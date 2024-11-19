
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

