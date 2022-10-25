# Contains all variables used within the FESOM-Mesh
# Import standard python packages
# Sys
import sys
#---
# Append system paths to FESOM MESH here
#---
                
# Data import
from netCDF4 import Dataset, MFDataset
                
# Data storage
import collections
import pandas as pd
                
# Math & Stats
import numpy as np
import math
import scipy as sc
import scipy.stats as stats
from scipy.io import netcdf
from scipy.interpolate import griddata
import random
                
# Plotting data
import matplotlib
import matplotlib.pylab as plt
import matplotlib.pyplot as plotter
from matplotlib.backends.backend_pdf import PdfPages
import colormap
import seawater as sw
from mpl_toolkits.basemap import Basemap

#---
# Some more FESOM Mesh modules
#---

# Hack to fix missing PROJ4 env var
import os
import conda
conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

#---
# Set the path to the mesh
#---
meshpath  = your_mesh_path

#---
# Load mesh
#---
#print("mesh will be loaded")
mesh=load_mesh(meshpath)

# Upload mesh-variables
result_path=path_to_original_data
    
#---
# Usually here the FESOM mesh is loaded
#---

# Create coordinates of centroids
elem_x = x_centroid_coordinate
elem_y = x_centroid_coordinate
    
def elem_neighbours():
    """
    Description:
        Returns all centroid-neighbours c' of a centroid c. Neighbouring centroids share a
        common edge, i.e. two same nodes within the grid. 
        This function has no boundary conditions, i.e. includes triangles c' wrapping
        around the channel as neighbours of c.
    Returns: 
        elem_neighbours (np.array), shape:(3,elem_n): Each centroid c contains of
        maximal 3 neighbours c'.
    """
    el = elem # Nodes of centroids
    el_n = elem_n
    elem_neighbours = np.zeros(shape=(3,el_n))
    
    for c in range(el_n):
        # Initialize
        nodes_c = el[:,c] # Nodes of specific centroid
        
        # Sets with same nodes as cell c
        A = np.where(el == nodes_c[0])[1] 
        B = np.where(el == nodes_c[1])[1]
        C = np.where(el == nodes_c[2])[1]
        
        # Intersection gives neighbouring cells c' of c, 
        # Setdiff subtracts c of this s
        n1 = np.setdiff1d(np.intersect1d(A,B), c)
        n2 = np.setdiff1d(np.intersect1d(A,C), c)
        n3 = np.setdiff1d(np.intersect1d(B,C), c)
        
        # Put all neighbour cells c' in one set
        neighbours = np.union1d(np.union1d(n1,n2), n3)
        neighbours = neighbours.astype('float')
        
        # Save neighbours to shape=(3,) array for saving to elem_neighbours
        neighbour = np.zeros(shape=3, dtype='float')
        neighbour[:] = np.nan
        index = 0
        for n in neighbours:
            neighbour[index] = n
            index = index + 1
        
        elem_neighbours[:, c] = neighbour
    
    return elem_neighbours   

def elem_neighbours_bc():
    """
    Documentation: 
        Returns all centroid-neighbours c' of a centroid c. Neighbouring centroids share a
        common edge, i.e. two same nodes within the grid. 
        This function includes boundary conditions, i.e. excludes triangles c' wrapping
        around the channel as neighbours of c.
    RETURN: 
        elem_neighbours (np.array), shape:(3,elem_n), Each centroid c contains of
        maximal 3 neighbours c'.
    """
    el = elem # Nodes of centroids
    el_n = elem_n
    elem_neighbours = np.zeros(shape=(3,el_n))
    
    for c in range(el_n):
        # Initialize
        nodes_c = el[:,c] # Nodes of specific centroid
        
        # Sets with same nodes as cell c
        A = np.where(el == nodes_c[0])[1] 
        B = np.where(el == nodes_c[1])[1]
        C = np.where(el == nodes_c[2])[1]
        
        # Intersection gives neighbouring cells c' of c, 
        # Setdiff subtracts c of this s
        n1 = np.setdiff1d(np.intersect1d(A,B), c)
        n2 = np.setdiff1d(np.intersect1d(A,C), c)
        n3 = np.setdiff1d(np.intersect1d(B,C), c)
        
        # Put all neighbour cells c' in one set
        neighbours = np.union1d(np.union1d(n1,n2), n3)
        neighbours = neighbours.astype('float')
        
        # Left boundary
        if c in left_boundary:
            index = 0
            for n in neighbours:
                if n in right_boundary:
                    neighbours[index] = np.nan # If a neighbour wraps around, set to NaN
                index = index + 1
        # Right boundary        
        if c in right_boundary:
            index = 0
            for n in neighbours:
                if n in left_boundary:
                    neighbours[index] = np.nan
                index = index + 1
        
        # Save neighbours to shape=(3,) array for saving to elem_neighbours
        neighbour = np.zeros(shape=3, dtype='float')
        neighbour[:] = np.nan
        index = 0
        for n in neighbours:
            neighbour[index] = n
            index = index + 1
        
        elem_neighbours[:, c] = neighbour
    
    return elem_neighbours