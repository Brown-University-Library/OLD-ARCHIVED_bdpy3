# -*- coding: utf-8 -*-

import json, logging, os, pprint
import requests
from . import logger_setup
from .auth import Authenticator


log = logging.getLogger(__name__)
logger_setup.check_logger()


class Searcher( object ):
    """ Enables easy calls to the BorrowDirect search webservice.
        BorrowDirect 'FindIt Web Service' docs: <https://relais.atlassian.net/wiki/display/ILL/Find+Item>
        Called by BorrowDirect.run_search() """

    def __init__( self ):
        self.valid_search_types = [ 'ISBN', 'ISSN', 'LCCN', 'OCLC', 'PHRASE' ]

    def search_exact_item( self, patron_barcode, api_url_root, api_key, partnership_id, university_code, search_type, search_value ):
        """ Searches for exact key-value.
            Called by BorrowDirect.run_search() """
        assert search_type in self.valid_search_types
        authorization_id = self.get_authorization_id( patron_barcode, api_url_root, api_key, partnership_id, university_code )
        # params = self.build_exact_item_params( partnership_id, university_code, patron_barcode, search_type, search_value )
        params = self.build_exact_item_params( patron_barcode, partnership_id, university_code, search_type, search_value )
        url = '%s/dws/item/available?aid=%s' % ( api_url_root, authorization_id )
        headers = { 'Content-type': 'application/json' }
        r = requests.post( url, data=json.dumps(params), headers=headers, timeout=90 )
        log.debug( 'search r.url, `%s`' % r.url )
        log.debug( 'search r.content, `%s`' % r.content.decode('utf-8') )
        result_dct = r.json()
        return result_dct

    def get_authorization_id( self, patron_barcode, api_url_root, api_key, partnership_id, university_code ):
        """ Obtains authorization_id.
            Called by search()
            Note that only the authenticator webservice is called;
              the authorization webservice simply extends the same id's session time and so is not needed here. """
        log.debug( 'starting get_authorization_id()...' )
        authr = Authenticator()
        authorization_id = authr.authenticate(
            patron_barcode, api_url_root, api_key, partnership_id, university_code )
        return authorization_id

    def build_exact_item_params( self, patron_barcode, partnership_id, university_code, search_type, search_value ):
        """ Builds search json.
            Called by search() """
        params = {
            'PartnershipId': partnership_id,
            'ExactSearch': [ {
                'Type': search_type, 'Value': search_value } ]
                }
        log.debug( 'params, `%s`' % pprint.pformat(params) )
        return params

    # end class Searcher
