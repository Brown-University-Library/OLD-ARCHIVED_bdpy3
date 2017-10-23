# -*- coding: utf-8 -*-

import os, pprint, time
from bdpy3 import BorrowDirect

""" Assumes bdpy3 has already been pip-installed, as per the main README.md """


print( 'exact-search example...' )
search_defaults = {
    'API_URL_ROOT': os.environ['BDPY3_SAMPLE_SCRIPT__API_URL_ROOT'],
    'API_KEY': os.environ['BDPY3_SAMPLE_SCRIPT__API_KEY'],
    'PARTNERSHIP_ID': os.environ['BDPY3_SAMPLE_SCRIPT__PARTNERSHIP_ID'],
    'UNIVERSITY_CODE': os.environ['BDPY3_SAMPLE_SCRIPT__UNIVERSITY_CODE']
    }
bd = BorrowDirect( search_defaults )
patron_barcode = os.environ['BDPY3_SAMPLE_SCRIPT__PATRON_BARCODE']
bd.run_search_exact_item( patron_barcode, 'ISBN', '9780688002305' )
print( 'exact-search-result...' ); pprint.pprint( bd.search_result )
print( '---' ); print( ' ' )
time.sleep( 1 )  # being nice to the server


print( 'bib-search example...' )
search_defaults = {
    'API_URL_ROOT': os.environ['BDPY3_SAMPLE_SCRIPT__API_URL_ROOT'],
    'API_KEY': os.environ['BDPY3_SAMPLE_SCRIPT__API_KEY'],
    'PARTNERSHIP_ID': os.environ['BDPY3_SAMPLE_SCRIPT__PARTNERSHIP_ID'],
    'UNIVERSITY_CODE': os.environ['BDPY3_SAMPLE_SCRIPT__UNIVERSITY_CODE']
    }
bd = BorrowDirect( search_defaults )
patron_barcode = os.environ['BDPY3_SAMPLE_SCRIPT__PATRON_BARCODE']
( title, author, year ) = ( 'Zen and the art of motorcycle maintenance - an inquiry into values', ['Pirsig, Robert M'], '1974' )
bd.run_search_bib_item( patron_barcode, title, author, year )
print( 'bib-search-result...' ); pprint.pprint( bd.search_result )
print( '---' ); print( ' ' )
time.sleep( 1 )  # being nice to the server


print( 'exact-request example...' )
## Will really generate request if item is requestable
request_defaults = {
    'API_URL_ROOT': os.environ['BDPY3_SAMPLE_SCRIPT__API_URL_ROOT'],
    'API_KEY': os.environ['BDPY3_SAMPLE_SCRIPT__API_KEY'],
    'PARTNERSHIP_ID': os.environ['BDPY3_SAMPLE_SCRIPT__PARTNERSHIP_ID'],
    'UNIVERSITY_CODE': os.environ['BDPY3_SAMPLE_SCRIPT__UNIVERSITY_CODE'],
    'PICKUP_LOCATION': os.environ['BDPY3_SAMPLE_SCRIPT__PICKUP_LOCATION']
    }
bd = BorrowDirect( request_defaults )
patron_barcode = os.environ['BDPY3_SAMPLE_SCRIPT__PATRON_BARCODE']
# bd.run_request_exact_item( patron_barcode, 'ISBN', '9780688002305' )
print( 'request_result...' ); pprint.pprint( bd.request_result )


print( 'bib-request example...' )
## Will really generate request if item is requestable
request_defaults = {
    'API_URL_ROOT': os.environ['BDPY3_SAMPLE_SCRIPT__API_URL_ROOT'],
    'API_KEY': os.environ['BDPY3_SAMPLE_SCRIPT__API_KEY'],
    'PARTNERSHIP_ID': os.environ['BDPY3_SAMPLE_SCRIPT__PARTNERSHIP_ID'],
    'UNIVERSITY_CODE': os.environ['BDPY3_SAMPLE_SCRIPT__UNIVERSITY_CODE'],
    'PICKUP_LOCATION': os.environ['BDPY3_SAMPLE_SCRIPT__PICKUP_LOCATION']
    }
bd = BorrowDirect( request_defaults )
patron_barcode = os.environ['BDPY3_SAMPLE_SCRIPT__PATRON_BARCODE']
( title, author, year ) = ( 'Zen and the art of motorcycle maintenance - an inquiry into values', ['Pirsig, Robert M'], '1974' )
# bd.run_request_bib_item( self.patron_barcode, title, author, year )
print( 'bib-request_result...' ); pprint.pprint( bd.bib_request_result )
