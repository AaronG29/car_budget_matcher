"""
This module will be used to test the user recommendations
"""

from car_data import CarDatabase


# can make this more efficient

class TestRecommendations():
    """Tests user preference recommendations"""

    def setup_method(self):
        self.db = CarDatabase()
        success = self.db.load_data("carvana.csv")
        assert success, "Failed to load carvana.csv"
    
    def test_recommendation_budget(self):
        """Test making sure that cars will match the users budget range"""
        # This is where the test will go
        result = self.db.filter_by_budget(16000, 24000)
        assert all(10000 <= float(car['Price']) <= 20000 for car in result)
    
    def test_recommendation_make(self):
        """Test making sure that cars will match the users make/makes"""
        # This is where the test will go
        pass

    def test_recommendation_year(self):
        """Test making sure that cars will match the users year"""
        # This is where the test will go
        pass

    
    def test_sort_by_recommendation(self):
        """Test that cars are sorted"""
        # This is where the test will go
        pass