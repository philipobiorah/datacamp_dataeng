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

# Print rows with consistent data
print(airlines[~cat_clean_rows])

# checking value consistency
# check for leading or trailing white spaces
demographics = demographics['marriage_status'].str.strip()
demographics['marriage_status'].value_counts()

# Collapsing data into categories

group_names = ['0-200K', '200K-500K', '500K+']
demographics['income_group'] = pd.qcut(demographics['household_income'], q = 3, labels = group_names)

# Print income group column
demographics[['income_group', 'household_income']]
#Using cut() to categorize data
# Create ranges for categories
ranges = [0, 200000, 500000, np.inf]
group_names = ['0-200K', '200K-500K', '500K+']
# Create income group column 
demographics['income_group'] = pd.cut(demographics['household_income'], bins = ranges, labels = group_names)

#print unique values of the column
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

#Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from dest_size column
airlines['dest_size'] = airlines['dest_size'].str.strip() 

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, labels = label_names)
# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 'Thursday': 'weekday', 'Friday': 'weekday', 'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)


# Fixing the phone number column
# Replace "+" with  "00"
phones["Phone number"] = phones["Phone number"].str.replace("+", "00")

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")


# Assert that full_name has no honorifics
# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False





# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])
