# -*- coding: utf-8 -*-

""" Configures logger if needed. """

import json, logging, logging.config, os, pprint


DEFAULT_CONFIG_DCT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}


def check_logger():
    """ Allows a log config dct to be passed in.
        Useful for logging to a file, or adjusting levels via settings.
        Called by most bdpy3 modules. """
    if not logging._handlers:
        config_dct = json.loads( os.environ.get('BDPY3_LOG_CONFIG_JSON', json.dumps(DEFAULT_CONFIG_DCT)) )
        print( 'config_dct, ```%s```' % pprint.pformat(config_dct) )
        logging.config.dictConfig( config_dct )
        return
