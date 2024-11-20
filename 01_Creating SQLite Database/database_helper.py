import sqlite3
import pandas as pd
import os
import time

class DatabaseHelper:
    def __init__(self, db_path='../database/mmdt.db3', retries=5, delay=1):
        """
        Initializes the DatabaseHelper instance with the given parameters.
        
        :param db_path: Path to the database file
        :param retries: Number of retries if the file cannot be deleted
        :param delay: Delay in seconds before retrying
        """
        self.db_path = db_path
        self.retries = retries
        self.delay = delay

    def delete_existing_db(self):
        """
        Deletes an existing database file if it exists.
        
        :return: True if file is successfully deleted, False otherwise
        """
        for _ in range(self.retries):
            try:
                if os.path.exists(self.db_path):
                    os.remove(self.db_path)
                    print(f"Existing database '{self.db_path}' deleted.")
                    return True
                else:
                    print("Database file does not exist.")
                    return False
            except PermissionError as e:
                print(f"Error: {e}. Retrying in {self.delay} seconds...")
                time.sleep(self.delay)
        print(f'Failed to delete database after {self.retries} tries')  
        return False

    def create_db(self, csv_file_paths=None):
        """
        Creates a new SQLite database and inserts data from CSV files into the database.
        
        :param csv_file_paths: A dictionary with table names as keys and CSV file paths as values
        :return: None
        """
        if csv_file_paths is None:
            csv_files = {
            'participants': './data/mmdt_selected_batch01.csv',
            'status': './data/mmdt_current_batch01.csv'
            }

        if self.delete_existing_db():
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            for table, csv_file_path in csv_file_paths.items():
                df = pd.read_csv(csv_file_path)
                df.to_sql(table, conn, if_exists='replace', index=False) #This create the schema for you. 
                print(f"Table '{table}' created and data inserted successfully.")

            conn.commit()
            conn.close()

            print("Database creation and data insertion completed successfully.")
