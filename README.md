# Project Description

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