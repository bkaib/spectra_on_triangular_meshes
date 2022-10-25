def total_dis_orig(u, udis, v, vdis):
    """
    Description:
        Calculates mean dissipation in the channel from original velocities u,v and dissipation tendencies udis, vdis.
        The dissipation in each grid cell is weighted by its area.
    Parameters:
        u, v (np.array): Horizontal velocities, Shape:(days, elem_n, nz)
        udis, vdis (np.array): Horizontal dissipation tendencies, shape:(days, elem_n, nz)
    Output:
        dis (np.array): Spatial Mean dissipation in the channel averaged over amount of days, shape=(nz,)
    """
    
    #- Modules
    from eddies.grid import FESOM_grid
    import numpy as np 
    
    #- Weights according to elem area
    weights = FESOM_grid.elem_area / np.sum(FESOM_grid.elem_area) # Area of elements / Total Area
    
    #- Calculate dissipation
    dis = u * udis + v * vdis
    dis = np.swapaxes(dis, 1, 2) # Swap axes to multiply weights
    dis = dis * weights # Weight DIS by area
    dis = np.mean(np.sum(dis, axis=2), axis=0) # Sum over all elements, take mean over all days  
    
    return dis

def total_ke_orig(u, v):
    """
    Description:
        Calculates mean Kinetic Energy in the channel from original velocities u,v.
        The Kinetic Energy in each grid cell is weighted by its area.
    Parameters:
        u, v (np.array): Horizontal velocities, shape:(days, elem_n, nz)
    Returns:
        ke (np.array): Spatial Mean Kinetic Energy in the channel averaged over amount of days, shape=(nz,)
    """
    
    #- Modules
    from eddies.grid import FESOM_grid
    import numpy as np 
    
    #- Weights according to elem area
    weights = FESOM_grid.elem_area / np.sum(FESOM_grid.elem_area) # Area of elements
    
    #- Calculate dissipation
    ke = (1 / 2) * (u ** 2 + v ** 2)
    ke = np.swapaxes(ke, 1, 2) # Swap axes to multiply weights
    ke = ke * weights # Weight KE by area
    ke = np.mean(np.sum(ke, axis=2), axis=0) # Sum over all elements, take mean over all days  
    
    return ke

def total_dis_interp(ui, udisi, vi, vdisi, grid_spacing):
    """
    Description:
        Calculates mean dissipation in the channel from interpolated velocities u,v and dissipation tendencies udis, vdis.
        The dissipation in each grid cell is weighted by its area.
    Parameters:
        ui, vi (np.array): Interpolated horizontal velocities, shape:(days, ny, nx, nz)
        udisi, vdisi (np.array): Horizontal dissipation tendencies, shape:(days, ny, nx, nz)
        grid_spacing (np.array): Grid_spacing of the interpolated rectangular (dx=dy) channel in degrees.
    Returns:
    dis (np.array): Spatial Mean dissipation in the (interpolated) channel averaged over amount of days, shape=(nz,)
    """
    #- Modules
    import numpy as np
    
    #- Parameters
    deg2km    = 111
    km2m      = 10 ** 3
    dx        = grid_spacing * deg2km * km2m # Rectangle sidelength in m
    ny        = ui.shape[1]
    nx        = ui.shape[2]
    nz        = ui.shape[3]
    elem_area = np.ones(shape=(ny, nx, nz)) * dx ** 2 # Area of each element in the interpolated grid
    weights   = elem_area / np.sum(elem_area, axis=(0,1)) 
    
    #- Calculate total dissipation
    dis = np.nansum((ui * udisi + vi * vdisi) * weights, axis=(1,2)) # Sum over nx and ny gridpoints and skip nan values
    dis = np.mean(dis, axis=0) # Mean over days
    
    return dis

def total_ke_interp(ui, vi, grid_spacing):
    """
    Description:
        Calculates mean Kinetic Energy in the channel from interpolated velocities u,v.
        The Kinetic Energy in each grid cell is weighted by its area.
    Parameters:
        ui, vi (np.array): interpolated horizontal velocities, shape:(days, elem_n, nz)
        grid_spacing (np.array): grid_spacing of the interpolated rectangular (dx=dy) channel in degrees.
    Returns:
        ke (np.array): Spatial Mean Kinetic Energy in the (interpolated) channel averaged over amount of days, shape=(nz,)
    """
    #- Modules
    import numpy as np
    
    #- Parameter
    deg2km    = 111
    km2m      = 10 ** 3
    dx        = grid_spacing * deg2km * km2m # Rectangle sidelength in m
    ny        = ui.shape[1]
    nx        = ui.shape[2]
    nz        = ui.shape[3]
    elem_area = np.ones(shape=(ny, nx, nz)) * dx ** 2 # Area of each element in the interpolated grid
    weights   = elem_area / np.sum(elem_area, axis=(0,1)) 

    #- Calculate total dissipation
    ke = np.nansum((1 / 2) * (ui ** 2 + vi ** 2) * weights, axis=(1,2)) # Sum over nx and ny gridpoints and skip nan values
    ke = np.mean(ke, axis=0) # Mean over days
    
    return ke