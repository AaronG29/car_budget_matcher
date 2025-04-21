"""
Module for the car dataset

This module will
-Load the car dataset
-Filter/Sort car dataset
"""

class CarDatabase:
    """
    Class for the CarDatabase
    
    Attributes:
        data (list): disctionary for car list
        filters (dict): filters for car data
    """
    
    def load_data(self, filepath):
        """
        Loads the car data from a file
        
        Args:
            filepath (str): the path to car data file
            
        Returns:
            bool: will be true is the load is successful, if not it will be false
        """
        # need to work on code and car data file