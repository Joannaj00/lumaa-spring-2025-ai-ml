import os
from pathlib import Path

class Config:
    """Configuration settings for the recommendation system"""
    # Paths
    ROOT_DIR = Path(__file__).parent.parent
    DATA_DIR = ROOT_DIR / "data"
    
    # Model parameters
    N_RECOMMENDATIONS = 5
    RANDOM_STATE = 42
    MIN_DF = 2
    MAX_FEATURES = 5000
    
    # File paths
    PERFUME_DATA_PATH = DATA_DIR / "perfume.csv"
    
    @staticmethod
    def get_env_variable(name, default=None):
        return os.getenv(name, default)