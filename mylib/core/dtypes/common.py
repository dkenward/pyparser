
def mylib_dtype(dtype):
    '''
    Converts input to an equivalent mylib dtype if possible.
    
    Parameters
    ----------
    dtype: object to be converted
    
    Returns
    -------
    np.dtype or mylib dtype
    
    Raises
    ------
    TypeError if not a dtype
    
    '''
    
    _dtypes = {
    'u': 'uint',
    'i': 'int',
    'c': 'complex',
    'f': 'float',
    'b': 'bool',
    'V': 'void',
    'O': 'object',
    'M': 'datetime',
    'm': 'timedelta'
    }
    