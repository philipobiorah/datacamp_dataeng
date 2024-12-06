#strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')
#convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')
#output: 0    47
#1    30
#2    41

# Write an assert statemtn making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration
print(ride_sharing['duration_time'])  
print(ride_sharing['duration_time'].mean())  