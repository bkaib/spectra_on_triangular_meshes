def scatter_plot_ratios():
    """
    Description:
        Example of how to scatterplot ratios (ORIG / INTERPOLATED) of dissipation and kinetic energy.
    """
    #- Modules
    import numpy as np
    from eddies.data import data_manager
    from eddies.figures import plotter
    
    #- Parameters
    dx1       = 0.09 #- Grid Spacings of interpolated Grid
    dx2       = 0.045
    dx3       = 0.01
    methods   = ['nearest', 'linear','cubic'] # Interpolation methods
    
    #- Generate Random Data used for plotting
    #- 0.09
    total_dis1 = np.abs(np.random.randn(3)) # sx1 
    total_dis2 = np.abs(np.random.randn(3)) # sx2
    total_ke1 = np.abs(np.random.randn(3)) # sx1 
    total_ke2 = np.abs(np.random.randn(3)) # sx2
    
    #- 0.045
    total_dis3 = np.abs(np.random.randn(3)) # sx1 
    total_dis4 = np.abs(np.random.randn(3)) # sx2
    total_ke3 = np.abs(np.random.randn(3)) # sx1 
    total_ke4 = np.abs(np.random.randn(3)) # sx2
    
    #- 0.01
    total_dis5 = np.abs(np.random.randn(3)) # sx1 
    total_dis6 = np.abs(np.random.randn(3)) # sx2
    total_ke5 = np.abs(np.random.randn(3)) # sx1 
    total_ke6 = np.abs(np.random.randn(3)) # sx2
    
    #- Enter Ratios to dictionary for each grid-spacing
    dis_ratios  = np.concatenate((total_dis1, total_dis2)) 
    ke_ratios   = np.concatenate((total_ke1, total_ke2))
    dx009_dict  = data_manager.create_gridspacing_dict(dis_ratios, ke_ratios)
    
    dis_ratios  = np.concatenate((total_dis3, total_dis4))
    ke_ratios   = np.concatenate((total_ke3, total_ke4))
    dx0045_dict  = data_manager.create_gridspacing_dict(dis_ratios, ke_ratios)
    
    dis_ratios  = np.concatenate((total_dis5, total_dis6))
    ke_ratios   = np.concatenate((total_ke5, total_ke6))
    dx001_dict  = data_manager.create_gridspacing_dict(dis_ratios, ke_ratios)
    
    #- Add all grid spacings dictionaries to a dictionary with all ratios
    dictionaries  = [dx009_dict, dx0045_dict, dx001_dict]
    grid_spacings = np.array([0.09, 0.045, 0.01])
    energy_ratios = data_manager.create_energyratios_dict(dictionaries, grid_spacings)
    
    #- Scatter Plot ratios
    fig = plotter.scatter_energy_ratios(energy_ratios)
    fig.show()
    
    return(energy_ratios)