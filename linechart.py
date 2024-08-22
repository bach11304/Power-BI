import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('ProductDetail.csv')

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['product_id'], df['unit_price'])

# Add labels and title
plt.xlabel('Product ID')
plt.ylabel('Unit Price')
plt.title('Product Unit Prices Over Time')

# Display the chart
plt.show()

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['product_id'], df['unit_price'], label='Unit Price')
plt.plot(df['product_id'], df['stock_quantity'], label='Stock Quantity')
plt.plot(df['product_id'], df['unit_cost'], label='Unit Cost')

# Add labels and title
plt.xlabel('Product ID')
plt.ylabel('Value')
plt.title('Product Metrics Over Time')
plt.legend()

# Display the chart
plt.show()