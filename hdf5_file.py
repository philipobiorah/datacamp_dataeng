# Description: This script reads the data from the hdf5 file.
import h5py
filename = 'LIGO_data.hdf5'
data = h5py.File(filename, 'r')
print(type(data))


# The structure of HDF5 file is similar to that of a dictionary. The keys are the names of the datasets and the values are the datasets themselves.
for key in data.keys():
    print(key)

    #output: meta, quality, strain

# Get the HDF5 group: group
group = data['strain']
# Check out keys of group
for key in group.keys():
    print(key)

    #output: Strain

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')

plt.show()

# Close file
data.close()

#output: <class 'h5py._hl.files.File'>

#meta
#quality

#Strain

#<class 'numpy.ndarray'>


#output: <class 'h5py._hl.files.File'>

#meta
#quality
#strain



#St