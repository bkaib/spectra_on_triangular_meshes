def save_interpolated_values(u, udis, v, vdis, year, scheme, dx, dy, sx, sy, folder, method, interp_boarders):
    """
    Description: 
        Saves interpolated values to specified folder at disk.
    Parameters:
        u, udis, v, vdis (np.array): Values to save
        year (int): Year of interpolated data
        scheme (str): Backscatter scheme
        dx, dy, sx, sy (float): Target-Grid spacing and starting points for interpolation
        folder (str): Location where to save data
        method (str): Interpolation method
        interp_boarders (bool): If NaN values on the edges are interpolated by nearest neigbours or cut out
    Returns:
    Saved data at disk
    f1, f2, f3, f4: filenames, type:str
    """
    
    #- Modules
    import numpy as np
    
    #- Saving
    save = 'y' #input('Want to save (y/n)?')
    if save == 'y':
        if interp_boarders == True:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'filled_boarders'
                   )
        else:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method
                   )
            
        f1 = folder + 'u_'    + flag #- Filenames
        f2 = folder + 'udis_' + flag
        f3 = folder + 'v_'    + flag
        f4 = folder + 'vdis_' + flag
        
        np.save(f1, u)
        print('u saved to {}'.format(f1))
        np.save(f2, udis)
        print('udis saved to {}'.format(f2))
        np.save(f3, v)
        print('v saved to {}'.format(f3))
        np.save(f4, vdis)
        print('vdis saved to {}'.format(f4))
        
        print('All data saved')
        return (f1, f2, f3, f4)
    else:
        print('No data saved')
        return(None, None, None, None)
    
def save_collapsed_spectra(ke, dis, year, scheme, dx, dy, sx, sy, folder, method, is_hw, interp_boarders):
    """
    Description: 
        Saves collapsed spectra to specified folder at disk.
    Parameters:
        ke, dis (np.array): Values to save
        year (int): Year of interpolated data 
        scheme (str): Backscatter scheme, 
        dx, dy, sx, sy (float): Target-Grid spacing and starting points for interpolation
        folder (str): location where to save data
        method (str): interpolation method
        is_hw (bool): if a Hanning Window was applied to data
    Returns:
        Saved data at disk
        f1, f2, f3, f4 (str): filenames
    """
    
    #- Modules
    import numpy as np
    
    #- Saving
    save = 'y' # input('Want to save (y/n)?')
    if save == 'y':
        if is_hw == True and interp_boarders == False:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'hw'
                   )
        elif is_hw == True and interp_boarders == True:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'hw' + '_'
                    + 'filled_boarders'
                   )
        elif is_hw == False and interp_boarders == True:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'filled_boarders'
                   )
        else:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method                                       
                   )            
            
        f1 = folder + 'collapsed2D_KE_'  + flag #- Filenames
        f2 = folder + 'collapsed2D_DIS_' + flag
        
        np.save(f1, ke)
        print('KE saved to {}'.format(f1))
        np.save(f2, dis)
        print('DIS saved to {}'.format(f2))
        
        print('All data saved')
        
        return (f1, f2)
    
    else:
        print('No data saved')
        
        return(None, None)

def save_total_energetics_interpolated(ke, dis, year, scheme, dx, dy, sx, sy, folder, method, is_hw, interp_boarders):
    """
    Description: 
        Saves total dissipation and kinetic energy of interpolated channel to specified folder at disk.
    Parameters:
        ke, dis (np.array): Values to save
        year (int): Year of interpolated data 
        scheme (str): Backscatter scheme, 
        dx, dy, sx, sy (float): Target-Grid spacing and starting points for interpolation
        folder (str): location where to save data
        method (str): interpolation method
        is_hw (bool): if a Hanning Window was applied to data
    Returns:
        Saved data at disk
        f1, f2, f3, f4 (str): filenames
    """
    
    #- Modules
    import numpy as np
    
    #- Saving
    save = 'y' #input('Want to save (y/n)?')
    if save == 'y':
        if is_hw == True and interp_boarders == False:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'hw'
                   )
        elif is_hw == True and interp_boarders == True:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'hw' + '_'
                    + 'filled_boarders'
                   )
        elif is_hw == False and interp_boarders == True:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method + '_'
                    + 'filled_boarders'
                   )
        else:
            flag = (scheme + '_' +  str(year) + '_' 
                    + str(np.round(dx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(dy, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sx, decimals=4)).replace('.','c') + '_' 
                    + str(np.round(sy, decimals=4)).replace('.','c') + '_'
                    + method                                       
                   )              
            
        f1 = folder + 'total_energetics_ke_interp_'  + flag #- Filenames
        f2 = folder + 'total_energetics_dis_interp_' + flag
        
        np.save(f1, ke)
        print('KE saved to {}'.format(f1))
        np.save(f2, dis)
        print('DIS saved to {}'.format(f2))
        
        print('All data saved')  
    else:
        print('No data saved')