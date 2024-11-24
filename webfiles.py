
from urllib.request import urlretrieve


import pandas as pd

# Assign url of file: url
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

# Save file locally]
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')

print(df.head())
#output:

#    fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \

# 0            7.4              0.70         0.00             1.9      0.076

# reading excel web file
# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name=None)

# Print the sheetnames to the shell
print(xls.keys())
#output: dict_keys(['1700', '1900'])

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())
#output:    country       1700  1701  1702  1703  1704  1705  1706  1707  1708  ...  \  
# 0  Afghanistan  34.5650   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  ...
# 1      Albania  41.0000   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  ...
# 2      Algeria  36.7500   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  ...
# 3      Andorra  42.5075   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  ...
