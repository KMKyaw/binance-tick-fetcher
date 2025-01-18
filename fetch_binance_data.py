import os
import requests
import zipfile
import pandas as pd

def get_tick_data(asset: str, date: str) -> pd.DataFrame:
    """
    Processes the tick CSV for a specific asset and date, and returns the DataFrame

    Parameters:
        asset (str): The asset symbol (e.g., 'BTCUSDT')
        date (str): The date in 'yy-mm-dd' format (e.g., '25-01-16')

    Returns:
        DataFrame with columns ['Time', 'Volume', 'Price', 'Asset']
    """

    year, month, day = date.split("-")
    file_name = f"{asset}-trades-20{year}-{month}-{day}.zip"
    base_url = f"https://data.binance.vision/data/spot/daily/trades/{asset}/"
    url = f"{base_url}{file_name}"
    
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)
    file_path = os.path.join(download_dir, file_name)
    unzip_dir = os.path.join(download_dir, "unzipped")
    os.makedirs(unzip_dir, exist_ok=True)
    
    try:
        # Step 1: Download the file
        print(f"Downloading {file_name}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):  # Download in chunks
                file.write(chunk)
        print(f"Downloaded successfully: {file_path}")
    
        # Step 2: Unzip the file
        print(f"Unzipping {file_name}...")
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(unzip_dir)
        print(f"Unzipped successfully to: {unzip_dir}")
    
        # Step 3: Process the CSV
        csv_file = next(f for f in os.listdir(unzip_dir) if f.endswith(".csv"))
        csv_path = os.path.join(unzip_dir, csv_file)
        df = pd.read_csv(csv_path, header=None)
        filtered_df = df.iloc[:, [1, 2, 4]]
        filtered_df.columns = ["Price", "Volume", "Time"]
        filtered_df["Asset"] = asset[:3]
        filtered_df = filtered_df[["Time", "Volume", "Price", "Asset"]]
        processed_file_path = os.path.join(download_dir, f"{asset}_processed_{date}.csv")
        filtered_df.to_csv(processed_file_path, index=False)
        print(f"Processed CSV saved to: {processed_file_path}")
        os.remove(file_path)
        os.remove(csv_path)
        os.rmdir(unzip_dir)
        print(f"Cleaned up temporary files: {file_path} and {csv_path}")
        return filtered_df
    except Exception as e:
        print(f"Error occurred: {e}")
        return pd.DataFrame()

