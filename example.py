from fetch_binance_data import get_tick_data

# Fetch and process data for BTCUSDT on January 16, 2025
df = get_tick_data("BTCUSDT", "25-01-16")

# Display the first few rows of the DataFrame
print(df.head())