def get_wavenumbers(n):
    """
    Description:
    Returns ordered wavenumbers as they appear when using np.fft.fft() tool
    
    Input:
    n: integer, number of elements over which to perform FFT
    
    Output:
    k, vector containing positive and negative wavenumbers
    """
    #- Modules
    import numpy as np
    
    #- Parameter
    k = np.arange(0, n)

    #- Calculate Wavenumbers
    if n%2 == 0: # Even
        k[-(n//2)+1:] = - np.flip(k[1:(n//2)]) # NF sits in the middle (see np.fft.fft()?)
    else: # Odd
        k[-(n//2):] = - np.flip(k[1:(n//2)+1])
        
    return k