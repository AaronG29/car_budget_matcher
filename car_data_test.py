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
        """Test for making sure that the data will load right"""
        assert len(self.db.data) == 4
        assert self.db.data[0]["Name"] == "Mazda 5"
    
    def test_budget(self):
        """Test for filtering the cars by their max price"""
        results = self.db.filter_by_budget(5000, 15000)
        car_names = [car["Name"] for car in results]
        assert "Ford Focus" in car_names
        assert "Mazda 5" in car_names
        assert "Toyota Corolla" in car_names
        assert "Tesla Model Y" not in car_names

    def test_make(self):
        """Filter by the car make test"""
        results = self.db.filter_by_make(["toyota"])
        assert len(results) == 1
        assert results[0]["Name"] == "Toyota Corolla"

    def test_year(self):
        """Filter by the car min year test"""
        results = self.db.filter_by_year(2018, 2023)
        car_names = [car["Name"] for car in results]
        assert "Tesla Model Y" in car_names
        assert "Toyota Corolla" in car_names
        assert "Mazda 5" not in car_names
        assert "Ford Focus" not in car_names