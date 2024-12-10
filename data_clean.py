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




#Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date
#output: 0    2016-01-21

# save today's date
today = dt.date.today()

# set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

#print the maximum date in the ride_dt column
print(ride_sharing['ride_dt'].max())

# Find duplicates
duplicates = ride_sharing.duplicated(subset = 'ride_id',   keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])
#output: ride_id  duration  user_birth_year
#220  11   44  1983
#221  11
#222  11   44  1983
#223  11   44  1983
#224  11   44  1983
#225  11   44  1983
#226  11   44  1983



# find inconsistent data
# find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# print rows with inconsistent data
print(airlines[cat_clean_rows])