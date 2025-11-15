import psycopg2
import yaml
from dataclasses import dataclass
import os
import pandas as pd

@dataclass
class DatabaseConfig:
    """Dataclass to hold database configuration details.
    """

    dbname: str
    user: str
    password: str
    host: str
    port: str

class PostgresDB:
    """Class to handle PostgreSQL database connections and operations.
    
    Attributes:
        config (DatabaseConfig): Configuration details for the database connection.
        connection (psycopg2.extensions.connection or None): Active database connection.
    """

    def __init__(self, config_path ="/home/rohan/DataEngineering/mini_ETL_project/database.yml"):
        """Initializes the PostgresDB class with database configuration from a YAML file.
        
        Args:
            config_path (str): Path to the YAML file containing database configuration.
        """
        self.config_path = config_path
        self.config = DatabaseConfig(**self.load_db_config())
        self.connection = None

    def load_db_config(self):
        """Loads database configuration from a YAML file.
        
        """
        try:
            with open(self.config_path) as f:  # Corrected variable name
                config = yaml.safe_load(f)
                return config  # Fixed typo
        except FileNotFoundError as e:
            print(f"Configuration file not found: {e}")
            raise

    def connect(self):
        """Establishes a connection to the PostgreSQL database.
        
        """
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    dbname=self.config.dbname,
                    user=self.config.user,
                    password=self.config.password,
                    host=self.config.host,
                    port=self.config.port
                )
                print("Database connection established.")
            except psycopg2.Error as e:
                print(f"Error connecting to database: {e}")
                raise
    
    def disconnect(self):  # Fixed method name
        """Closes the database connection.
        
        """
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            print("Database connection closed.")

    def run_query(self, query: str) -> pd.DataFrame:
        """Executes a SQL query on the PostgreSQL database.
        
        Args:
            query (str): The SQL query to be executed.
        
        Returns:
            pd.DataFrame: The query execution result.
        """
        
        self.connect()
        result = None  # Initialize result variable
        
        try:
            with self.connection.cursor() as cursor:
                print(f"Executing query: {query}")
                cursor.execute(query)
                columns = [desc[0] for desc in cursor.description]
                data = cursor.fetchall()
                print(f"Number of rows fetched: {len(data)}")
                result = pd.DataFrame(data, columns=columns)
                return result  # Return here, before finally closes connection
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            raise
        finally:
            self.disconnect()

    def insert_dataframe(self, df: pd.DataFrame, table_name: str) -> None:
        """Inserts a DataFrame into a PostgreSQL table.
        
        Args:
            df (pd.DataFrame): The DataFrame to insert.
            table_name (str): Name of the target table.
        """
        self.connect()
        
        try:
            with self.connection.cursor() as cursor:
                # Get column names from DataFrame
                columns = ', '.join(df.columns)
                placeholders = ', '.join(['%s'] * len(df.columns))
                insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                
                # Insert each row
                for row in df.itertuples(index=False):
                    cursor.execute(insert_query, tuple(row))
                
                self.connection.commit()
                print(f"Successfully inserted {len(df)} rows into {table_name}")
                
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")
            self.connection.rollback()
            raise
        finally:
            self.disconnect()
