# This will be our app/websites main code
# This is what will eventually display the matches

from car_data import CarDatabase
from user_input import user_car_budget, user_car_make, user_car_year, user_car_miles

def main():
    print("\nWelcome to the Car Budget Matcher!")
    print("This project/code will help you find a car based on your preferences.\n")

    db = CarDatabase()
    if not db.load_data("carvana.csv"):
        print("Failed to load the car data -- Make sure carvana.csv is in the same folder.")
        return
    
    # Getting the users preferences...
    min_price, max_price = user_car_budget()
    makes = user_car_make()
    min_year, max_year = user_car_year()
    min_miles, max_miles = user_car_miles()

# Filters here...
    results = db.filter_by_budget(min_price, max_price)
    results = db.filter_by_make(makes)
    results = db.filter_by_year(min_year, max_year)
    results = db.filter_by_miles(min_miles, max_miles)