import pandas as pd

df = pd.read_csv('Customer.csv')

print(df)

print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Handle missing values
df.dropna(subset=['customer_id', 'first_name', 'last_name', 'email'], inplace=True)

# Check for and remove duplicate rows
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Standardize data formats
df['registration_date'] = pd.to_datetime(df['registration_date'])