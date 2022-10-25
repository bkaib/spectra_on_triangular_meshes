def regular_grid(lx, ly, dx, dy, sx, sy):
    """
    Description: 
        Creates a regular grid.
    Parameters:
        lx, ly (float): length in zonal and meridional direction
        dx, dy (float): stepsize in zonal and meridional direction
        sx, sy (float): starting values zonal and meridional direction 
    Returns:
        XX, YY (np.array): Coordinates of a regular grid in meshgrid format
    """
    import numpy as np
    
    xx = np.arange(sx, lx, dx) # Coordinates of regular grid
    yy = np.arange(sy, ly, dy)
    
    XX, YY = np.meshgrid(xx, yy) # Grid
    
    return (XX, YY)