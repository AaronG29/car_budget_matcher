"""
This module will test the car database and filters
"""

from car_data import CarDatabase

class TestCarDatabase():
    """Test for CarDatabase class"""

    def setup_method(self):
        """Setup for the test data before the test run"""
        self.db = CarDatabase()
        self.db.data = [
            {"Name": "Mazda 5", "Year": "2016", "Miles": "50000", "Price": "11000"},
            {"Name": "Tesla Model Y", "Year": "2022", "Miles": "10000", "Price": "45000"},
            {"Name": "Toyota Corolla", "Year": "2020", "Miles": "30000", "Price": "15000"},
            {"Name": "Ford Focus", "Year": "2012", "Miles": "90000", "Price": "7000"}
        ]
        

    def test_data(self):
        """Test that data works"""
        # This is where the test will go
        pass
    
    def test_budget(self):
        """Test that cars can be filtered by price"""
        # This is where the test will go
        pass

    def test_make(self):
        """Test that cars can be filtered by make"""
        # This is where the test will go
        pass
    
    def test_year(self):
        """Test that cars can be filtered by year"""
        # This is where the test will go
        pass