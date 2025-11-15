#load csv file into dataframe
# transform/clean the data
# load the data to postgresql db

import pandas as pd
from database import PostgresDB
from pathlib import Path
from data_modeling import data_loader,data_transformer



def main():
    # Define the path to the CSV file
   file_path = Path.home() /"DataEngineering" / "mini_ETL_project" / "data" / "world_cups.csv"
   df = data_loader(file_path)
   df = data_transformer(df)
   db = PostgresDB()  
   db.insert_dataframe(df, table_name="world_cup_summary")

   print("ETL process completed successfully.")

if __name__ == "__main__":
    main()