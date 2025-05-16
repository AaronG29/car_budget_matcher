"""
Module for the car dataset

This module will
-Load the car dataset
-Filter/Sort car dataset
"""

# We will be pulling information (data) from Carvana

import csv



class CarDatabase:
    """
    Class for the CarDatabase
    
    Attributes:
        data: dictionary for car list
        filters: filters for car data
    """
    def __init__(self):
        self.data = []
    
    def load_data(self, filepath):
        """
        Loads the car data from our carvana.csv file
        
        args: filepaththe path to car data file
        returns: bool, will be true is the load is successful, it will turn out as false if it's not
        """

        try:
            with open(filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def filter_by_budget(self, min_price, max_price, cars=None):
        """
        Filters a list of cars based off the price that the users inputs

        args: 
        min_price: user min price they set
        max_price: user max price they set

        returns: the filtered list of cars within the users specified budget
        """
        if cars is None:
            cars = self.data
        filtered = []
        for car in cars:

            try:
                price = float(car['Price'])
                if min_price <= price <= max_price:
                    filtered.append(car)
            except (ValueError, KeyError):
                continue
        return filtered

    def filter_by_make(self, makes, cars=None):
        """
        Filters a list of cars based off the make of the car that the users inputs

        args: 
        makes: lowercas car name to match one of the car makes availible

        returns: the filtered list with the names of the make/makes that are availible
        """
        if cars is None:
            cars = self.data
        filtered = []
        for car in cars:

            try:
                make = car['Name'].split()[0].lower()
                if make in makes:
                    filtered.append(car)
            except (KeyError, IndexError):
                continue
        return filtered
    
    def filter_by_year(self, min_year, max_year, cars=None):
        """
        Filters a list of cars based off the year that the users inputs

        args: 
        min_year: user min year they set
        max_year: user max year they set

        returns: the filtered list of cars within the users specified years
        """
        if cars is None:
            cars = self.data
        filtered = []
        for car in cars:

            try:
                year = int(car['Year'])
                if 1900 <= year <= 2025 and min_year <= year <= max_year:
                    filtered.append(car)
            except (ValueError, KeyError):
                continue
        return filtered
    
    def filter_by_miles(self, min_miles, max_miles, cars=None):
        """
        Filters a list of cars based off the miles that the users inputs

        args: 
        min_miles: user min miles they set
        max_miles: user max miles they set

        returns: the filtered list if cars within the users specified miles
        """
        if cars is None:
            cars = self.data
        filtered = []
        for car in cars:

            try:
                miles = int(car['Miles'])
                if min_miles <= miles <= max_miles:
                    filtered.append(car)
            except (ValueError, KeyError):
                continue
        return filtered
    
    def sort_results(self, cars, sort_key='Price', reverse=False):
        """
        List of car dict based off the key

        args: 
        sort_key: how the sorting will occur, whether its by: price, make, year, milage, etc.

        returns: sorted list of car dictionaries
        """
        try:
            return sorted(cars, key=lambda car: float(car[sort_key]), reverse=reverse)
        except (KeyError, ValueError):
            return cars