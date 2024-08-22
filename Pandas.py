import pandas as pd

# Function to handle missing values
def handle_missing_values(df):
    """
    Handles missing values in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to process.

    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """
    # Replace missing values in numeric columns with the mean
    for col in df.select_dtypes(include=['number']):
        df[col].fillna(df[col].mean(), inplace=True)

    # Replace missing values in categorical columns with the most frequent value
    for col in df.select_dtypes(include=['object']):
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df

# Function to handle data errors
def handle_data_errors(df):
    """
    Handles data errors in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to process.

    Returns:
        pd.DataFrame: The DataFrame with data errors handled.
    """
    # Convert columns to appropriate data types
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                pass

    # Handle inconsistent data formats
    # ... (add specific error handling logic based on the data)

    return df

# Load the CSV files
customer_df = pd.read_csv("customer table_csv.txt")
product_detail_df = pd.read_csv("product detail_csv.txt")
product_group_df = pd.read_csv("product group_csv.txt")
data_market_trend_df = pd.read_csv("dataMarketTrend_CSV.txt")

# Handle missing values and data errors using Pandas methods
customer_df = customer_df.fillna(customer_df.mean())  # Fill numeric missing values with mean
customer_df = customer_df.fillna(customer_df.mode().iloc[0])  # Fill categorical missing values with mode
customer_df = customer_df.apply(pd.to_numeric, errors='ignore')  # Convert columns to numeric where possible

product_detail_df = product_detail_df.fillna(product_detail_df.mean())
product_detail_df = product_detail_df.fillna(product_detail_df.mode().iloc[0])
product_detail_df = product_detail_df.apply(pd.to_numeric, errors='ignore')

product_group_df = product_group_df.fillna(product_group_df.mean())
product_group_df = product_group_df.fillna(product_group_df.mode().iloc[0])
product_group_df = product_group_df.apply(pd.to_numeric, errors='ignore')

data_market_trend_df = data_market_trend_df.fillna(data_market_trend_df.mean())
data_market_trend_df = data_market_trend_df.fillna(data_market_trend_df.mode().iloc[0])
data_market_trend_df = data_market_trend_df.apply(pd.to_numeric, errors='ignore')

# Demo of the processed data
print("Customer Data:")
print(customer_df.head())
print("\nProduct Detail Data:")
print(product_detail_df.head())
print("\nProduct Group Data:")
print(product_group_df.head())
print("\nData Market Trend Data:")
print(data_market_trend_df.head())
