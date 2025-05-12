"""
Module for the car dataset

This module will
-Load the car dataset
-Filter/Sort car dataset
"""

# We will be pulling information (data) from Cargurus and Carvana

import csv



class CarDatabase:
    """
    Class for the CarDatabase
    
    Attributes:
        data (list): disctionary for car list
        filters (dict): filters for car data
    """
    def __init__(self):
        self.data = []
    
    def load_data(self, filepath):
        """
        Loads the car data from a file
        
        Args:
            filepath (str): the path to car data file
            
        Returns:
            bool: will be true is the load is successful, if not it will be false
        """

        try:
            with open(filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
        
        # need to work on code and car data file

    # def budget_filtering (1st filtering option I thought of)

    # def make_filtering

    # def model_filtering

    # def year_filtering

    # def results_filtering