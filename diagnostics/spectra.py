def get_2D_spectrum(u, v, udis, vdis):
    """
    Description:
        Applies 2D-Fourier Transformation in zonal and meridional direction. Calculates Kinetic Energy and Dissipation Spectrum.
        Collapses 2D-Spectrum of Diagnostics to 1D.
    Parameters:
        u, v (np.array): zonal velocities, shape:(days, ny, nx, nz)
        udis, vdis (np.array): dissipation tendencies, shape:(days, ny, nx, nz)
    Returns:
        ske_collapsed, sd_collapsed (np.array): Collapsed 2D-Spectra
        states (np.array): Wavenumber vector containing all wavenumbers used in each iteration of collapsing process
    """
    #- Modules
    import numpy as np
    from eddies.common import fourier_tools
    
    #- Parameters
    days = u.shape[0]
    ny   = u.shape[1] # number of meridional gridpoints
    nx   = u.shape[2] # number of zonal gridpoints
    nz   = u.shape[3] # number of vertical gridpoints
    
    #- 2D-Fourier Transform
    fu    = np.fft.fft2(u, axes=(1,2)) # FFT applied in meridional and zonal direction
    fv    = np.fft.fft2(v, axes=(1,2))
    fudis = np.fft.fft2(udis, axes=(1,2))
    fvdis = np.fft.fft2(vdis, axes=(1,2))  
    
    #- Energy Diagnostics
    ske = np.real(fu * np.conj(fu) + fv * np.conj(fv)) / (2 * ny ** 2 * nx ** 2)   # Kinetic Energy
    sd  = np.real(fu * np.conj(fudis) + fv * np.conj(fvdis)) / (ny ** 2 * nx ** 2) # Dissipation
    
    #- Reduce to positive wavenumbers k+ including Nyquist Frequency and k=0, e.g. DC-component
    #- Positive k in first half of all axes (see docs of np.fft.fft2)
    ske[:, 1:ny//2+1, 1:nx//2+1, :] = 2 * np.real(ske[:, 1:ny//2+1, 1:nx//2+1, :])  # Leave out DC. +1 to include NF.
    sd[:, 1:ny//2+1, 1:nx//2+1, :]  = 2 * np.real(sd[:, 1:ny//2+1, 1:nx//2+1, :])   # If nx,ny are odd or even does not matter
    
    ske = ske[:, :ny//2+1, :nx//2+1, :] # Keep all wavenumber up to NF
    sd  = sd[:, :ny//2+1, :nx//2+1, :]
       
    #- Compute isotropic spectrum
    states         = [] # saves all collapsedsed wavenumbers
    kmax_collapsed = int(np.round(np.sqrt( (nx // 2 + 1) ** 2 + (ny // 2 + 1) ** 2))) # Number of max. collapsed wavenumber
    ske_collapsed  = np.zeros(shape=(days, kmax_collapsed, nz)) # collapsedsed 2d Spectra
    sd_collapsed   = np.zeros(shape=(days, kmax_collapsed, nz)) 
    
    for ky in range(ny//2+1): # meridional
        for kx in range(nx//2+1): # zonal
            kk = int(np.round(np.sqrt(kx ** 2 + ky ** 2))) # Round up for values >= .5, 
            ske_collapsed[:, kk,:] = ske_collapsed[:, kk, :] + ske[:, ky, kx, :]
            sd_collapsed[:, kk, :] = sd_collapsed[:, kk, :] + sd[:, ky, kx, :]
            states.append(kk)
    
    states = np.array(states)
    
    return (ske_collapsed, sd_collapsed, states)