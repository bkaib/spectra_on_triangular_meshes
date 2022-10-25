# Project Description - Scale analysis on unstructured grids: Kinetic energyand dissipation power spectra on triangular meshes
## Plain Language Summary
To better understand the physical processes that drive and define the circulation 
in our oceans, it is necessary to analyse the temporal and spatial scales on which these processes act. 
A classical method to investigate the spatial scale behaviour is the Fourier analysis which splits any given data into waves of different amplitudes and wavelengths.
Mathematically this requires data on an equidistantly spaced grid. However, many ocean models apply triangular or other irregular grids for their computations of oceanic flows.
In this study, we describe the advantages and disadvantages of applying Fourier analysis for models that use triangular meshes, with prior interpolation of data to regularly spaced rectangular meshes. We also introduce two other methods that can analyse the distribution of kinetic energy and kinetic energy dissipation across scales without interpolation. The results show that one needs to be very careful when choosing a specific scale analysis and, potentially, an interpolation method for triangular grids, especially when it comes to analysing the process of kinetic energy dissipation.

# Structure

- common (package): Contains calculational tools used during preprocessing of data

- data (package): Tools to load, save and manage data. Make sure adjust filepaths of the loading and saving module. The data manager is used to massage data in order to fit into other modules.

- diagnostics (package): Tools to calculate the energetics and collapsed 2d-spectra of kinetic energy and dissipation tendency.

- figures (package): Handles generated data and plots it in already preprocessed ways.

- grid (package): Functions to setup your specific grid (in our cases FESOM) as well as a regular grid (setup_grid.py)

- interpolation (package): Handles everything around the interpolation from the specific grid to the regular grid.

- main (folder): The main folder with commented Jupyter Notebooks and examples. 

- resources (folder): Sample folder holding your data to process.

Note: If a module can not be found, make sure to set the sys-path in all __init__.py files as shown in eddies/__init__.py.

# Launch
You can use the notebooks in main/ in order to reproduce results or apply the routines to your data.
