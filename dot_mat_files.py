# Import package scipy.io
import scipy.io

# Load MATLAB file: mat (mat is a dictionary)
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat 

print(type(mat))
#output: <class 'dict'>

# Print the keys of the dictionary mat
print(mat.keys())
#output: dict_keys(['__header__', '__version__', '__globals__', 'rfpCyt', 'rfpNuc', 'cfpNuc', 'cfpCyt', 'yfpNuc', 'yfpCyt', 'CYratioCyt'])

# Print the type of the value corresponding to the key 'CYratioCyt' in mat
print(type(mat['CYratioCyt']))  

#output: <class 'numpy.ndarray'>
# Print the shape of the value corresponding to the key 'CYratioCyt' in mat
print(mat['CYratioCyt'].shape)
#output: (200, 137)

# Subset the array and plot it
import matplotlib.pyplot as plt
import numpy as np

data = mat['CYratioCyt'][25, 5:]

