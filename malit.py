import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('ProductDetail.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['unit_price'], df['stock_quantity'])
plt.title('Relationship between Price and Stock Quantity')
plt.xlabel('Price')
plt.ylabel('Stock Quantity')
plt.show()