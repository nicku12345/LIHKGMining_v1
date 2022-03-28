"""
A file containing customized exceptions.
"""

class BadRequest(Exception):
    '''
    Customized exception used for throwing bad requests
    '''

class ExternalApiIsNotUniqueException(Exception):
    '''
    Customized exception used in fetching external apis
    '''

class ExternalApiRequestException(Exception):
    '''
    Customized exception used in fetching external apis
    '''
