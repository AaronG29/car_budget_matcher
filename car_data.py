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
    
    def filter_by_budget(self, min_price, max_price):

        filtered = []
        for car in self.data:
            try:
                price = float(car['Price'])
                if min_price <= price <= max_price:
                    filtered.append(car)
            except (ValueError, KeyError):
                continue
        return filtered

    def filter_by_make(self, makes):
        filtered = []
        for car in self.data:
            try:
                make = car['Name'].split()[0].lower()
                if make in makes:
                    filtered.append(car)
            except (KeyError, IndexError):
                continue
        return filtered
    
    def filter_by_year(self, min_year, max_year):
        filtered = []
        for car in self.data:
            try:
                year = int(car['Year'])
                if 1900 <= year <= 2025 and min_year <= year <= max_year:
                    filtered.append(car)
            except (ValueError, KeyError):
                continue
        return filtered
    
    def filter_by_miles(self, min_miles, max_miles):
        filtered = []
        for car in self.data:
            try:
                miles = int(car['Miles'])
                if min_miles <= miles <= max_miles:
                    filtered.append(car)
            except (ValueError, KeyError):
                continue
        return filtered
    
    def sort_results(self, cars, sort_key='Price', reverse=False):
        try:
            return sorted(cars, key=lambda car: float(car[sort_key]), reverse=reverse)
        except (KeyError, ValueError):
            return cars