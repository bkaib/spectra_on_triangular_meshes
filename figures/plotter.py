def compare_original_interpolated(u_matrix, u_int, day, lvl, xx, yy):
    """
    Description: 
        Plots original and interpolated values next to each other.
    Parameters:
        u_matrix (np.array): Original values in matrix form, shape(days, ny, nx, lvl)
        u_int (np.array)   : Interpolated values in matrix form, shape(days,ny, nx, lvl)
        xx, yy (np.array)  : Coordinates of the plot, shape:(elem,)
    
        Note: u_matrix should contain the same number of levels as u_int. Make sure which
        levels were interpolated.
    Returns:
        fig: figure of original and interpolated values using imshow(). 
    """
    
    #- Modules
    import matplotlib.pyplot as plt
    import numpy as np
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,20))
    
    ax[0].imshow(u_matrix[day,:,:-1,lvl], extent=(0, np.max(xx), 0, np.max(yy)), origin='lower')
    ax[0].set_title('Original')
    ax[1].imshow(u_int[day,:,:,lvl], extent=(0, np.max(xx), 0, np.max(yy)), origin='lower')
    ax[1].set_title('Interpolated')
    
    return fig

def scatter_energy_ratios(energy_ratios, scheme=None, marker=None):
    """
    Description:
        Creates a scatter plot of energy ratios (Dis, Ke) of Original and interpolated 
        grid depending on the gridsize of the latter.
    Parameters:
        energy_ratios (dict): Nested dictionary with energy ratios containing grid-spacings as keys.
        
            Example: 
            energy_ratios = {'dx1' : dx1_dict, 'dx2' : dx2_dict}
            dx1_dict     = {'dis' : total_dissipation_ratios, 'ke': total_ke_ratios}
            total_dissipation_ratios, original / interpolated total dissipation, np.array(), shape(3*n), n = amount of starting values (sx, sy) for gridspacing dx1
            Ratios are expected to be in following order: ['nearest', 'linear', 'cubic'] * n
        scheme (str): Which scheme was used
        marker (str): Marker for scatter plot
    Returns:
        fig: Scatter Plot
    """
    #- Import Modules
    import matplotlib.pyplot as plt
    import numpy as np
    
    #- Parameters
    grid_spacings = []
    for grid_spacing in energy_ratios.keys(): 
        grid_spacings.append(grid_spacing)
        
    n       = len(energy_ratios[grid_spacings[0]]) # Number of starting values per grid spacing
    methods = ['Nearest', 'Linear','Cubic'] # Used for x-axis labeling
    x       = [1, 2, 3] * n #- Where to scatter plot values of methods
    m       = len(methods)
    if marker == None:
        marker = np.arange(1, len(energy_ratios.keys())+1).astype(str)

    
    #- Error handling   
    for d in energy_ratios.values():
        assert (len(d['dis']) % 3) == 0, 'Function expects a ratio for each method of [nearest, linear, cubic].'
        assert (len(d['ke']) % 3) == 0, 'Function expects a ratio for each method of [nearest, linear, cubic].'
        
    #- Canvas
    fig, ax = plt.subplots(1, 2, figsize=(10,5))
    title = 'ORIG/INTERP-Ratios'
    if scheme is not None:
        title = title + ' ' + scheme
        
    fig.suptitle(title)
    ax[0].set_title('Dissipation')
    ax[1].set_title('Kinetic Energy')
    
    # X-labels
    ax[0].set_xticks(range(1,4))
    ax[0].set_xticklabels(methods)
    ax[1].set_xticks(range(1,4))
    ax[1].set_xticklabels(methods)
    
    #- Plot Values
    i = 0
    for grid_dict in energy_ratios.values():
        ax[0].scatter(x, grid_dict['dis'], marker=marker[i], label=grid_spacings[i])
        ax[1].scatter(x, grid_dict['ke'],  marker=marker[i], label=grid_spacings[i])
        i = i + 1
    
    #- Legend  
    leg = ax[1].legend()
    for marker in leg.legendHandles:
        marker.set_color('black')
        
    return fig