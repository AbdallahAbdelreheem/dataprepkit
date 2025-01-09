import pandas as pd
import numpy as np
from typing import Union
df=pd.read_csv('C:\\projects\\dataprepkit\\fifa_eda.csv')
class DataPrepKit:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def read_data(self, file_path: str) -> pd.DataFrame:
    
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            return pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            return pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV, Excel, or JSON file.")

    def print_statistical_summaries(self) -> None:
        
        # Calculate the average values for numeric columns
        average_values = self.df.mean(numeric_only=True)

        # Calculate the most frequent values for all columns
        most_frequent_values = self.df.mode().iloc[0]

        print("Average Values:")
        print(average_values)
        print("\nMost Frequent Values:")
        print(most_frequent_values)

    def handle_missing_values(self, strategy: str = 'drop', fill_value: Union[str, int, float] = None, columns: list = None) -> pd.DataFrame:
       
        if columns is None:
            columns = self.df.columns

        if strategy == 'drop':
            self.df = self.df.dropna(subset=columns)
        elif strategy == 'mean':
            for column in columns:
                if self.df[column].dtype in ['float64', 'int64']:
                    self.df[column].fillna(self.df[column].mean(), inplace=True)
        elif strategy == 'median':
            for column in columns:
                if self.df[column].dtype in ['float64', 'int64']:
                    self.df[column].fillna(self.df[column].median(), inplace=True)
        elif strategy == 'mode':
            for column in columns:
                self.df[column].fillna(self.df[column].mode()[0], inplace=True)
        elif strategy == 'constant':
            if fill_value is not None:
                self.df[columns] = self.df[columns].fillna(fill_value)
            else:
                raise ValueError("fill_value must be provided when strategy is 'constant'")
        else:
            raise ValueError("Unsupported strategy. Please choose from 'drop', 'mean', 'median', 'mode', 'constant'")

        return self.df

