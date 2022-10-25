def mult_along_axis(A, B, axis):
    """
    Description:
    Elementwise multiplication of vector B along a given axis of A
    
    Input:
    A, matrix
    B, vector
    
    Output:
    Matrix of same shape as A
    
    Author: 
    https://stackoverflow.com/questions/30031828/multiply-numpy-ndarray-with-1d-array-along-a-given-axis
    """
    #- Modules
    import numpy as np
    
    #- Ensure we're working with Numpy arrays
    A = np.array(A)
    B = np.array(B)

    #- Shape check
    if axis >= A.ndim:
        raise AxisError(axis, A.ndim)
    if A.shape[axis] != B.size:
        raise ValueError(
            "Length of 'A' along the given axis must be the same as B.size"
            )

    #- np.broadcast_to puts the new axis as the last axis, so 
    # we swap the given axis with the last one, to determine the
    # corresponding array shape. np.swapaxes only returns a view
    # of the supplied array, so no data is copied unnecessarily.
    shape = np.swapaxes(A, A.ndim-1, axis).shape

    #- Broadcast to an array with the shape as above. Again, 
    # no data is copied, we only get a new look at the existing data.
    B_brc = np.broadcast_to(B, shape)

    #- Swap back the axes. As before, this only changes our "point of view".
    B_brc = np.swapaxes(B_brc, A.ndim-1, axis)

    return A * B_brc