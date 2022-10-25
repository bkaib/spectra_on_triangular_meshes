def interpolate_to_grid(u, xx0, yy0, XX1, YY1, days, lvls, method):
    """
    Description: 
        Interpolates u from a grid of xx0, yy0 coordinates to a target grid of XX1, YY1 coordinates
        using a specified method (nearest, linear, cubic).
    Parameters: 
        u (np.array): quantity to interpolate, shape:(days, elem, lvl)
        xx0, yy0 (np.array): Coordinates of the original grid, shape: (elem,)
        XX1, YY1 (np.array): Coordinates of the target grid, shape: (ny, nx) or (ny, nx), 
        days (int): Last day to interpolate to starting from day=0
        lvls (int): Number of Levels in z-direction to analyze. Starting from lvl=0.
        method (str): Interpolation method (nearest, linear, cubic)
    Returns:
        u_interp (np.array): Interpolated quantity at target grid, shape:(day, ny, nx)
    """
    #- Modules
    from scipy.interpolate import griddata
    import numpy as np 
    
    #- Parameters
    ny = XX1.shape[0]
    nx = XX1.shape[1]
    u_interp = np.zeros(shape=(days, ny, nx, lvls))
    
    #- Interpolation
    print('Starting interpolation')
    for day in range(days):
        #print(f'Interpolate day {day + 1}')
        for lvl in range(lvls):
            #print(f'Interpolate lvl {lvl + 1}')
            u_interp[day,:,:, lvl] = griddata(points=(xx0, yy0), 
                                   values=u[day, :, lvl], 
                                   xi=(XX1, YY1),
                                   method=method
                      )
    print('Ending interpolation')
        
    return u_interp

def interpolate_to_grid_at_lvl(u, xx0, yy0, XX1, YY1, days, lvl, method):
    """
    Description: 
        Interpolates u at a certain level from a grid of xx0, yy0 coordinates to a 
        target grid of XX1, YY1 coordinates using a specified method (nearest, linear, cubic).
    Parameters: 
        u (np.array): quantity to interpolate, shape:(days, elem, lvl)
        xx0, yy0 (np.array): Coordinates of the original grid, shape: (elem,)
        XX1, YY1 (np.array): Coordinates of the target grid, shape: (ny, nx) or (ny, nx), 
        days (int): Last day to interpolate to starting from day=0
        lvl (int): Level in z-direction to analyze
        method (str): Interpolation method (nearest, linear, cubic)
    Returns:
        u_interp (np.array): Interpolated quantity at target grid, shape:(day, ny, nx)
    """
    #- Modules
    from scipy.interpolate import griddata
    import numpy as np 
    
    #- Parameters
    ny = XX1.shape[0]
    nx = XX1.shape[1]
    u_interp = np.zeros(shape=(days, ny, nx))
    
    #- Interpolation
    print('Starting interpolation')
    for day in range(days):
        print(f'Interpolate day {day + 1}')
        u_interp[day,:,:] = griddata(points=(xx0, yy0), 
                               values=u[day, :, lvl], 
                               xi=(XX1, YY1),
                               method=method
                  )
    print('Ending interpolation')
        
    return u_interp   
    