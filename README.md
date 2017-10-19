UNDER DEVELOPMENT
=================


### about ###

'bdpy3' is a python3 library that faciliates programmatic access to the API to [BorrowDirect](http://www.borrowdirect.org), an academic book-borrowing consortium.

We use this in production for our 15,000+ successful automated BorrowDirect requests each year -- _and_ for thousands more automated searches for items that are either unavailable or not-found.

on this page...

- installation
- common usage
- possible responses
- notes
- license



### installation ###

git clone, or pip install...

    $ pip install git+https://github.com/birkin/bdpy3

- best to install a 'release' version, though all code in the master branch can be expected to be stable.

- one dependency: the awesome [requests](http://docs.python-requests.org/en/latest/) module, which is automatically pip-installed if necessary



### common usage - search ###

- search via exact-item:

        >>> from bdpy3 import BorrowDirect
        >>> defaults = {
            'API_URL_ROOT': url, 'API_KEY': key, 'PARTNERSHIP_ID': id, 'UNIVERSITY_CODE': code }
        >>> bd = BorrowDirect( defaults )
        >>> bd.run_search_exact_item( patron_barcode, 'ISBN', '9780688002305' )
        >>> pprint( bd.search_result )

        {'Available': True,
         'OrigNumberOfRecords': 5,
         'PickupLocation': [{'PickupLocationCode': 'A',
                             'PickupLocationDescription': 'Rockefeller Library'}],
         'RequestLink': {'ButtonLabel': 'Request',
                         'ButtonLink': 'AddRequest',
                         'RequestMessage': 'Request this through Borrow Direct.'}}

- search via bib-item:

        >>> from bdpy3 import BorrowDirect
        >>> defaults = {
            'API_URL_ROOT': url, 'API_KEY': key, 'PARTNERSHIP_ID': id, 'UNIVERSITY_CODE': code }
        >>> bd = BorrowDirect( defaults )
        >>> ( title, author, year ) = ( 'Zen and the art of motorcycle maintenance - an inquiry into values', ['Pirsig, Robert M'], '1974' )
        >>> bd.run_search_bib_item( patron_barcode, title, author, year )
        >>> pprint( bd.request_result )

        {'Available': True,
         'OrigNumberOfRecords': 7,
         'PickupLocation': [{'PickupLocationCode': 'A',
                             'PickupLocationDescription': 'Rockefeller Library'}],
         'RequestLink': {'ButtonLabel': 'Request',
                         'ButtonLink': 'AddRequest',
                         'RequestMessage': 'Request this through Borrow Direct.'}}


### common usage - request ###

- request via exact-item:

        >>> from bdpy3 import BorrowDirect
        >>> defaults = {
            'API_URL_ROOT': url, 'API_KEY': key, 'PARTNERSHIP_ID': id, 'UNIVERSITY_CODE': code, 'PICKUP_LOCATION': location }
        >>> bd = BorrowDirect( defaults )
        >>> bd.run_request_exact_item( patron_barcode, 'ISBN', '9780688002305' )
        >>> pprint( bd.request_result )

        {'RequestNumber': 'BRO-12345678'}

- request via bib item:

        >>> from bdpy3 import BorrowDirect
        >>> defaults = {
            'API_URL_ROOT': url, 'API_KEY': key, 'PARTNERSHIP_ID': id, 'UNIVERSITY_CODE': code, 'PICKUP_LOCATION': location }
        >>> bd = BorrowDirect( defaults )
        >>> ( title, author, year ) = ( 'Zen and the art of motorcycle maintenance - an inquiry into values', ['Pirsig, Robert M'], '1974' )
        >>> bd.run_request_bib_item( patron_barcode, title, author, year )
        >>> pprint( bd.request_result )

        {'RequestNumber': 'BRO-12345678'}


### possible responses ###

- bd.search_result

        ## if found and available via borrowdirect...
        {'Available': True,
         'PickupLocation': [{'PickupLocationCode': 'A',
                             'PickupLocationDescription': 'Rockefeller Library'}],
         'RequestLink': {'ButtonLabel': 'Request',
                         'ButtonLink': 'AddRequest',
                         'RequestMessage': 'Request this through Borrow Direct.'},
         'SearchTerm': 'isbn=9780688002305'}

        ## found but held locally...
        {'Available': False,
         'RequestLink': {'ButtonLabel': 'View in the BROWN Library Catalog.',
                         'ButtonLink': 'http://josiah.brown.edu/record=.b18151139a',
                         'RequestMessage': 'This item is available locally.'}

        ## found but not available
        {'Available': False,
        'RequestLink': {'ButtonLabel': 'Request',
                       'ButtonLink': 'https://illiad.brown.edu/illiad/illiad.dll/OpenURL?genre=Book&sid=BD&HeldLocally=N&rft.title=The%20body%20and%20society&rft.aufirst=Peter%20Robert%20Lamont&rft.aulast=Brown&rft.edition=Twentieth%20anniversary%20ed.%20with%20a%20new%20introduction&rft.date=c2008&rft.isbn=9780231144063%20%28cloth%20%3A%20alk.%20paper%20%3A%20alk.%20paper%29&rft.isbn=9780231144070%20%28pbk.%20%3A%20alk.%20paper%20%3A%20alk.%20paper%29&rft.dat=195747707&rft.pub=Columbia%20University%20Press&rft.place=New%20York',
                       'RequestMessage': 'Place an interlibrary loan request via ILLiad.'},
        'SearchTerm': 'isbn=9780231144063'}

        ## if not found
        {"Problem":{"ErrorCode":"PUBFI002","ErrorMessage":"No result"}}

- bd.request_result

        ## if found and available via borrowdirect...
        {'RequestNumber': 'BRO-12345678'}

        ## found but held locally...
        {'RequestLink': {'ButtonLabel': 'View in the BROWN Library Catalog.',
                         'ButtonLink': 'http://josiah.brown.edu/record=.b18151139a',
                         'RequestMessage': 'This item is available locally.'}}

        ## found but not available
        {'RequestLink': {'ButtonLabel': 'Request',
                          'ButtonLink': 'https://illiad.brown.edu/illiad/illiad.dll/OpenURL?genre=Book&sid=BD&HeldLocally=N&rft.title=The%20body%20and%20society&rft.aufirst=Peter%20Robert%20Lamont&rft.aulast=Brown&rft.edition=Twentieth%20anniversary%20ed.%20with%20a%20new%20introduction&rft.date=c2008&rft.isbn=9780231144063%20%28cloth%20%3A%20alk.%20paper%20%3A%20alk.%20paper%29&rft.isbn=9780231144070%20%28pbk.%20%3A%20alk.%20paper%20%3A%20alk.%20paper%29&rft.dat=195747707&rft.pub=Columbia%20University%20Press&rft.place=New%20York',
                          'RequestMessage': 'Place an interlibrary loan request via ILLiad.'}}

        ## if not found
        {u'Problem': {u'ErrorCode': u'PUBRI003', u'ErrorMessage': u'No result'}}



### notes ###

- All searches and requests filter on format="Book". This meets our needs, but I can easily imagine other implementations, and may offer more flexibility regarding this in the future. Pull-requests welcome in the meantime.  :)

- BorrowDirect() instantiation is flexible: you can pass in a dict, a settings-module, a settings-module-path, or nothing (but then set the instance-attributes directly)

- no need to call the auth wrapper explicitly -- the calls to search and request do it automatically -- but you could if you wanted to:

        >>> from bdpy3 import BorrowDirect
        >>> defaults = {
            'API_URL_ROOT': url, 'API_KEY': key, 'PARTNERSHIP_ID': id, 'UNIVERSITY_CODE': code }
        >>> bd = BorrowDirect( defaults )
        >>> bd.run_auth_nz( patron_barcode )  # performs authN/Z & stores authorization-id
        >>> bd.AId  # authorization-id
        'abc...'
        >>> bd.authnz_valid
        True

- BorrowDirect [api documentation](https://relais.atlassian.net/wiki/display/ILL/Relais+web+services)
    - [auth](https://relais.atlassian.net/wiki/display/ILL/Authentication)
    - [searching](https://relais.atlassian.net/wiki/display/ILL/Find+Item)
    - [requesting](https://relais.atlassian.net/wiki/display/ILL/RequestItem)

- bdpy3 code contact: birkin_diana@brown.edu

- for a ruby library, see [jonathan rochkind's](https://github.com/jrochkind) comprehensive and well-tested [borrowdirect-api wrapper](https://github.com/jrochkind/borrow_direct)

- here is a [python2.x version of the library](https://github.com/Brown-University-Library/borrowdirect.py), no longer maintained (it does not search or request on title/author/date)

---

_( formatted in [markdown](http://daringfireball.net/projects/markdown/) )_
