import json
import os
from typing import List, Dict, Any

class DataService:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
    
    def load_data(self, filename: str) -> List[Dict[str, Any]]:
        """Load data from JSON file"""
        filepath = os.path.join(self.data_dir, filename)
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r') as file:
                    return json.load(file)
            return []
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_data(self, data: List[Dict[str, Any]], filename: str):
        """Save data to JSON file"""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data to {filename}: {e}")