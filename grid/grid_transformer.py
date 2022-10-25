def elem_to_matrix(u, yy):
    """
    Description:
        Transforms u-quantity given in element-structure to a matrix-structure consisting of 
        nx, ny gridpoints in zonal and meridional-direction, respectively. 
        All elements for one specific ny show triangles of same orientation (either up- or downwards).
        The counting of ny starts at the bottom of the channel, e.g. with the smallest y-value.
    
        Note: The FESOM-Grid is built in a strange way. For documentation see ??.
    Parameters:
        u (np.array): quantity on FESOM-grid, shape:(n_day, n_elem, n_lvl)
        yy (np.array): y-coordinates of quantity, shape:(n_elem,)
    Returns:
        u_grid (np.array): quantity in matrix-form, shape(n_day, ny, nx, n_lvl) 
    """
    
    #- Modules
    import numpy as np
    
    #- Parameters
    y_coord = np.unique(yy)
    n_day   = u.shape[0]
    n_elem  = u.shape[1]
    n_lvl   = u.shape[2]
    ny      = len(y_coord)
    nx      = n_elem // ny #- amount of elements / amount of y-coordinates = amount of x-coordinates
    u_grid  = np.zeros(shape=(n_day, ny, nx, n_lvl))
    
    #- Separate data by y-coordinate
    for i, y in enumerate(y_coord):
        u_grid[:, i, :, :] = u[:, np.where(yy == y)[0], :]
                    
    return u_grid