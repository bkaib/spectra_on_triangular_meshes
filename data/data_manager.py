def create_gridspacing_dict(dis_ratios, ke_ratios):
    """
    Description:
        Creates a dictionary with specific key values expected by function 'create_energyratios_dict()' in module 'energetics'.
    Parameters:
        dis_ratios (np.array): Ratios Orig / Interpolated for dissipation for one specific grid spacing
        ke_ratios (np.array): Ratios Orig / Interpolated for kinetic energy for one specific grid spacing
        
        Note: 
        Inputs must contain a ratio for each method: ['nearest', 'linear', 'cubic']
    Returns:
        (dict): Dictionary with specific keys for those ratios expected by function 'create_energyratios_dict()'.
    """
    #- Modules
    import numpy as np
    
    #- Exceptions
    assert len(dis_ratios) % 3 == 0, 'We need a ratio for each method [nearest, linear, cubic]'
    assert len(ke_ratios) % 3  == 0, 'We need a ratio for each method [nearest, linear, cubic]'

    return {'dis': dis_ratios, 'ke': ke_ratios}


def create_energyratios_dict(dictionaries, grid_spacings):
    """
    Description:
        Creates a dictionary of dictionaries containing dissipation and kinetic energy ratios for multiple grid spacings.
    Parameters:
        dictionaries (list): Contains (dict) with values for dissipation and kinetic energy. dictionaries.keys() are grid_spacings
        grid_spacings (np.array): Contains grid spacings
    Returns:
    (dict): A dictionary containing dissipation and kinetic energy ratios sorted by grid spacing. This dictionary can be used to produce
    a scatter plot by 'plotter' module and its function 'scatter_energy_ratios()'.
    """
    #- Modules
    import numpy as np 
    
    #- Exceptions
    assert len(dictionaries) == len(grid_spacings), 'There must be the same amount of gridspacing dictionaries as grid_spacings'
    
    #- Main
    grid_spacings = grid_spacings.astype(str)
    energy_ratios = {}
    for i,j in enumerate(grid_spacings):
        energy_ratios[j] = dictionaries[i]
        
    return energy_ratios