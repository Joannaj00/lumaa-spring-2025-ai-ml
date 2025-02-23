import pandas as pd
from .config import Config

class DataLoader:
    """Handle data loading and basic validation"""
    
    @staticmethod
    def load_perfume_data():
        """Load perfume dataset with basic validation"""
        try:
            df = pd.read_csv(Config.PERFUME_DATA_PATH, encoding="latin1")
            df = df.head(500) # take the first 500 rows (as said in the requirements)
            # print(df.head())
            required_columns = ['Name', 'Brand', 'Description', 'Notes']
            
            if not all(col in df.columns for col in required_columns):
                raise ValueError(f"Missing required columns: {required_columns}")
                
            return df
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {Config.PERFUME_DATA_PATH}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
