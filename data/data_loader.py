#----------------------
# Import modules for this package
#----------------------

def load_original_data(path, year, model_run):
    """
    Description:
        Loads original datasets of FESOM
    Parameters:
        path (str): Source of the original data. Must end with "/". 
        year (str): Year of the corresponding FESOM data
        model_run (str): Identifier for the datasource
    Returns: 
        u, udis, v, vdis (np.array): Velocities and dissipation tendency.
    """

    #---
    # Note: Implement this function such that it load data from your source path.
    #---
      
    return (u, udis, v, vdis)

def load_interpolated_total_energetics(f_dis, f_ke, filled=True):
    """
    Description: 
        Load total energetics of interpolated data for each method and returns it in one array
    Parameters:
        f_dis, f_ke (str): Description of the file
        filled (bool): whether NaN-values of interpolated data was filled at the boarder or not (Defaults:True)
    
    Output:
        dis_interp, ke_interp (np.arrays): Total energetics of dissipation or kinetic energy of interpolated data. Shape=(n_methods,)
    """
    #- Modules
    import numpy as np
    
    #- Exceptions
    assert type(f_dis) == str, 'Need a string as input'
    assert type(f_ke) == str, 'Need a string as input'
    
    #- Parameters
    folder     = '../resources/total_energetics_interpolated/'
    methods    = ['nearest', 'linear', 'cubic']
    
    #- Ratios for different starting values
    ke_interp  = np.zeros(len(methods)) 
    dis_interp = np.zeros(len(methods))
    
    #- Load all energetics for grid spacings
    for i, method in enumerate(methods):
        if filled == True:
            #- Grid of certain gridspacing
            ke_interp[i]  = np.load(folder + f_ke +  '_' + method  + '_' + 'filled_boarders.npy')
            dis_interp[i] = np.load(folder + f_dis +  '_' + method + '_' + 'filled_boarders.npy')       
        else:
            #- Grid of certain gridspacing
            ke_interp[i]  = np.load(folder + f_ke +  '_' + method  + '.npy')
            dis_interp[i] = np.load(folder + f_dis +  '_' + method + '.npy')
        
    return dis_interp, ke_interp