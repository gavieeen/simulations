import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    # Download historical data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def simulate_random_variation(prices):
    # Simulate random variation in prices (for demonstration)
    random_noise = np.random.normal(0, 5, len(prices))  # Gaussian noise with mean 0 and std deviation 5
    simulated_prices = prices + random_noise
    return simulated_prices

if __name__ == "__main__":
    # Parameters
    ticker_symbol = "NVDA"
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    # Fetch historical stock data
    stock_data = fetch_stock_data(ticker_symbol, start_date, end_date)
    
    # Extract closing prices
    prices = stock_data['Close'].values

    # Simulate random variation
    simulated_prices = simulate_random_variation(prices)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, prices, label='Original Prices', color='blue')
    plt.plot(stock_data.index, simulated_prices, label='Simulated Prices', color='red', linestyle='--')
    plt.title(f'Stock Prices and Simulated Variation ({ticker_symbol})')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()