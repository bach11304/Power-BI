import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Customer.csv')

plt.figure(figsize=(10, 6))
df.groupby(pd.to_datetime(df['registration_date']).dt.to_period('M'))['customer_id'].count().plot()
plt.title('Customer Registration Trend Over Time')
plt.xlabel('Registration Date')
plt.ylabel('Number of Customers')
plt.show()

plt.figure(figsize=(10, 6))
df.groupby(pd.to_datetime(df['registration_date']).dt.to_period('M'))['customer_id'].count().cumsum().plot()
df.groupby(pd.to_datetime(df['registration_date']).dt.to_period('M'))['customer_id'].count().plot()
plt.title('New Customers vs Cumulative Customers Over Time')
plt.xlabel('Registration Date')
plt.ylabel('Number of Customers')
plt.legend(['Cumulative Customers', 'New Customers'])
plt.show()