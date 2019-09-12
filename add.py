#define user-defned functions
class Error(Exception):
    '''Base class for other exceptions'''
    pass
class ValueTooSmallError(Error):
    '''Raised when the input value is ttoo small'''
    pass
class ValueTooLargeError(Error):
    '''Raised when the input value is too Large'''
    pass
