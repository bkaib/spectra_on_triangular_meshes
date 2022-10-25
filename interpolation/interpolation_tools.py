def apply_hanning_window(u, axis):
    """
    Description:
        Applies a Hanning Window along the given axis of u
    Parameters:
        u (np.array): Quantity in matrix form
        axis (int): Axis along which to apply hanning window 
    Returns:
        (np.array): Hanning window applied to u along axis
    """
    #- Modules
    import numpy as np
    from eddies.common import calculation_tools
    
    #- Hanning Window along given axis
    n_axis = u.shape[axis]
    hw     = np.hanning(n_axis)
    
    return(calculation_tools.mult_along_axis(u, hw, axis))

def cut_boarders(u_int):
    """
    Description:
        Cuts the white boarders (NaN-values) of interpolated quantity u_int given in the 
        channel until it does not contain any NaN values anymore.
    Parameters:
        u_int (np.array): interpolated data, shape(days, ny, nx, nz)
    Returns:
    u_int (np.array): interpolated data without NaN values, shape(days, bottom:-top, left:-right, nz)
    """
    #- Modules
    import numpy as np
    
    #- Parameters
    bottom = 1
    top    = 1
    left   = 1
    right   = 1
    
    #- Cut boarders
    while np.isnan(u_int).sum() != 0:
        u_int  = u_int[:, bottom:-top, left:-right, :]
        bottom = bottom + 1
        top    = top + 1
        left   = left + 1
        right  = right + 1
        
    return u_int

def fill_boarders(u_int):
    """
    Description:
        Fills the white boarders (NaN-values) of interpolated quantity u_int given in the 
        channel with values of its nearest neighbours by broadcasting.
    Parameters:
        u_int (np.array): interpolated data, shape(days, ny, nx, nz)
    Returns:
        u_int (np.array): interpolated data without NaN values, shape(days, ny, nx, nz) 
    """
    #- Modules
    import numpy as np
    
    if np.sum(np.isnan(u_int)) == 0:
        print('The quantity already has no NaN values')
        return (u_int)
    
    else:
        #- Setup
        nans      = np.array(np.where(np.isnan(u_int[0,:,:,0])))  # NaN values will be at same coordinates for all days and levels
        not_nans  = np.array(np.where(~np.isnan(u_int[0,:,:,0])))
        ny_isnan  = nans[0,:] #- y-coordinates of NaN
        nx_isnan  = nans[1,:]
        ny_valued = not_nans[0,:] # y-coordinates of values
        nx_valued = not_nans[1,:]
        
        #- Fill meridional boundaries except corners
        x1 = np.min(nx_valued) # Zonal area that is used to fill NaN values
        x2 = np.max(nx_valued)
        
        #-- Fill Bottom
        y1 = np.min(ny_isnan)
        y2 = np.min(ny_valued)
        
        for i in range(y1, y2+1):
            u_int[:, i, x1:x2, :] = u_int[:, y2, x1:x2, :]
        
        #-- Fill Top
        y1 = np.max(ny_valued)
        y2 = np.max(ny_isnan)
        
        for i in range(y1, y2+1):
            u_int[:, i, x1:x2, :] = u_int[:, y1, x1:x2, :]
          
        #- Fill zonal boundaries
        y1 = np.min(ny_valued) # Meridional area that is used to fill NaN values
        y2 = np.max(ny_valued)
        
        #-- Fill Left side
        x1 = np.min(nx_isnan)
        x2 = np.min(nx_valued)
        
        for i in range(x1, x2+1):
            u_int[:, y1:y2, i, :] = u_int[:, y1:y2, x2, :]
            
        #-- Fill Right side
        x1 = np.max(nx_valued)
        x2 = np.max(nx_isnan)
        
        for i in range(x1, x2+1):
            u_int[:, y1:y2, i, :] = u_int[:, y1:y2, x1,:]
        
        #- Fill the corners
        bottom  = 0
        top     = -1
        
        while np.sum(np.isnan(u_int)) != 0: 
            
            # Bottom left an right corners
            nans     = np.where(np.isnan(u_int[0, bottom, :, 0]))[0] # access array by [0] 
            not_nans = np.where(~np.isnan(u_int[0, bottom, :, 0]))[0]
            left     = np.min(not_nans)
            right    = np.max(np.where(not_nans))
            
            for i in nans:
                if i < left:
                    u_int[:, bottom, i, :] = u_int[:, bottom, left, :] # Bottom left corner
                elif i > right:
                    u_int[:, bottom, i, :] = u_int[:, bottom, right, :] # Bottom right corner
            
            bottom = bottom + 1
            
            # Top
            nans     = np.where(np.isnan(u_int[0, top, :, 0]))[0]
            not_nans = np.where(~np.isnan(u_int[0, top, :, 0]))[0] 
            left     = np.min(not_nans)
            right    = np.max(np.where(not_nans))
            
            for i in nans:
                if i < left:
                    u_int[:, top, i, :] = u_int[:, top, left, :] # Top left corner
                elif i > right:
                    u_int[:, top, i, :] = u_int[:, top, right, :] # Top right corner
                    
            top = top - 1
            
        return u_int

def fill_boarders_NN(u_int):
    """
    Description:
        Fills the white boarders (NaN-values) of interpolated quantity u_int given in the 
        channel with values of its nearest neighbour. Uses scipy's NearestNDInterpolator.
    Parameters:
        u_int (np.array): interpolated data, shape(days, ny, nx, nz)
    Returns:
        u_int (np.array): interpolated data without NaN values, shape(days, ny, nx, nz) 
    """
    #- Modules
    import numpy as np
    from scipy.interpolate import NearestNDInterpolator
    
    mask = np.where(~np.isnan(u_int)) # select data to update interpolator
    interp = NearestNDInterpolator(np.transpose(mask), u_int[mask]) # creates interpolator with valid data
    u_int  = interp(*np.indices(u_int.shape)) # interpolate all NaN values by nearest neighbour
    
    return u_int