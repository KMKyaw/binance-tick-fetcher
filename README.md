# Binance Data Fetcher 📊

A Python library to fetch and process tick data from Binance for a specified asset and date. This script downloads the data, processes it into a clean CSV format, and return pandas.DataFrame.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-2.x-yellow?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-orange?logo=pandas)

---

## Features

- 📦 **Download trade data**: Pull historical tick data for any asset supported by Binance.
- 🛠️ **Data processing**: Extracts essential columns (`Time`, `Volume`, `Price`, `Asset`) from the raw dataset.
- 🧹 **File cleanup**: Automatically removes temporary files (ZIP and raw CSV).
- 🔍 **Reusable function**: A modular function for easy integration into larger Python projects.

---

## Installation

### Prerequisites

- Python 3.7 or later
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

---

## Usage

### Example Code

Here’s how you can use the `get_tick_data` function:

```python
from fetch_binance_data import get_tick_data

# Fetch and process data for BTCUSDT on January 16, 2025
df = get_tick_data("BTCUSDT", "25-01-16")

# Display the first few rows of the DataFrame
print(df.head())
```

### Output

The processed data is returned as a `pandas.DataFrame` with the following structure:

| Time          | Volume | Price    | Asset |
| ------------- | ------ | -------- | ----- |
| 1673846399999 | 0.0023 | 20850.50 | BTC   |
| 1673846400000 | 0.0015 | 20851.00 | BTC   |

The columns are:

- `Time`: Timestamp of the trade (in milliseconds since epoch).
- `Volume`: Quantity of the asset traded.
- `Price`: Trade price of the asset in USDT.
- `Asset`: Asset symbol (e.g., `BTC`).

---

## Directory Structure

```
fetch_binance_data/
├── fetch_binance_data.py   # Main script with the fetch_and_process_data function
├── downloads/              # Directory for processed files
│   ├── BTCUSDT_processed_25-01-16.csv # processed csv
├── README.md               # Documentation
├── requirements.txt        # Dependencies
└── .gitignore              # Ignored files
```

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
