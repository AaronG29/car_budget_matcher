"""
This module will be used to test the user recommendations

Module looks at CarDatabase class and tests if the filtering works based on
user preference.

-budget filtering
-make filtering
-year filtering
-price filtering
"""

from car_data import CarDatabase



class TestRecommendations():
    """Tests user preference recommendations"""

    def setup_method(self):
        """Loads the carvana.csv dataset that will be used to make recommendations based on the cars in the datset"""
        self.db = CarDatabase()
        success = self.db.load_data("carvana.csv")
        assert success, "Failed to load carvana.csv"
    
    def test_recommendation_budget(self):
        """Test making sure that cars will match the users budget range"""
        result = self.db.filter_by_budget(16000, 24000)
        assert all(16000 <= float(car['Price']) <= 24000 for car in result)
    
    def test_recommendation_make(self):
        """Test making sure that cars will match the users make/makes"""
        result = self.db.filter_by_make(['toyota', 'honda'])
        assert all(car['Name'].split()[0].lower() in ['toyota', 'honda'] for car in result)

    def test_recommendation_year(self):
        """Test making sure that cars will match the users preferred year/years"""
        result = self.db.filter_by_year(2016, 2018)
        assert all(2016 <= int(car['Year']) <= 2018 for car in result)
        
    def test_sort_by_recommendation(self):
        """Test that cars are sorted, the sorting will be done by price (least/greatest -- cheapest car - most expensive car)"""
        cars = self.db.filter_by_budget(5500, 11000)
        assert cars, "No cars found in the budget"  

        sorted_result = self.db.sort_results(cars, sort_key='Price', reverse=False)
        prices = [float(car["Price"]) for car in sorted_result]
        assert prices == sorted(prices), "The cars are not sorted by their ascending prices" 