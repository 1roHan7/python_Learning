import pandas as pd
from pathlib import Path

def data_loader(file_path):
    """Extracts data from a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as e:
        print(f"CSV file not found: {e}")
        raise

def data_transformer(df):
    """Transforms and cleans the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame to be transformed.   
        """
    df = df.fillna(0)  # Example transformation: Fill NaN values with 0 
    df = df.rename(columns=lambda x: x.strip().lower().replace(' ', '_').replace('-', '_'))
    return df