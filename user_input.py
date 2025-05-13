"""
User input module for car prefences

This module will have the user input their prefered car name, year, miles price
"""

import datetime
import csv

def load_cars_from_csv(filename):
    car_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            car = {
                "name": row["Name"].strip(),
                "year": int(row["Year"]),
                "miles": int(row["Miles"]),
                "price": int(row["Price"].strip())
            }
            car_list.append(car)
    return car_list

def user_car_budget():
    """
    User will input their desired budget into the prompt
    
    Returns:
        tuple: both min_price and max_price
    
    Raises:
        ValueError: If the user inputs anything other than numbers or if the user's max is lower than their min
    """
    print("\nBudget Range Preferences:")
    
    # min price
    while True:
        try:
            min_price = float(input("Please enter your minimum price: $").strip())
            if min_price < 0:
                print("The price cannot be negative.")
                continue
            break
        except ValueError:
            print("A valid number is needed for your minimum price.")
    
    # max price
    while True:
        try:
            max_price = float(input("Please enter your maximum price: $").strip())
            if max_price < min_price:
                print(f"Maximum price needs to be greater than minimum price of (${min_price}).")
                continue
            break
        except ValueError:
            print("A valid number is needed for your maximum price.")
    
    return (min_price, max_price)


def user_car_make():
    """
    User will input their desired car make into the prompt

    Returns:
        list: String list to show user's preference on car makes
    """
    print("\nMake Preferences:")
    
    while True:
        makes_input = input("Please enter your preferred car make (Separate the makes by commas if more then one, e.g. Honda, Toyota, Mazda): ").strip()
        
        if not makes_input:
            print("At least one make is required to display a match.")
            continue
            
        makes_list = []
        for make in makes_input.split(','):
            cleaned_make = make.strip().lower()
            if cleaned_make:
                makes_list.append(cleaned_make)
                
        if makes_list: 
            return makes_list
            
        print("No valid make given")

def user_car_year():
    """
    User will input their desired car year range into the prompt
    
    Returns:
        tuple: both minimum_year and maximum_year (integers)
    """
    print("\nYear Range Preferences:")
    current_year = datetime.datetime.now().year
    
    # min year
    while True:
        try:
            min_year = int(input(f"Enter minimum preferred year (1900-{current_year}): ").strip())
            if min_year < 1900 or min_year > current_year:
                print(f"The year must be between 1900 and {current_year}.")
                continue
            break
        except ValueError:
            print("Not a valid minimum year")

    # max year
    while True:
        try:
            max_year = int(input(f"Enter maximum preferred year ({min_year}-{current_year}): ").strip())
            if max_year < min_year or max_year > current_year:
                print(f"Year must be between {min_year} and {current_year}.")
                continue
            break
        except ValueError:
            print("Not a valid maximum year")
    
    return (min_year, max_year)

def filter_cars(car_list, min_price, max_price, preferred_makes, min_year, max_year):
    filtered = []
    for car in car_list:
        name = car["name"].lower()
        year = car["year"]
        price = car["price"]

        if (min_price <= price <= max_price and
            min_year <= year <= max_year and
            any(make in name for make in preferred_makes)):
            filtered.append(car)

    return filtered

def user_car_miles():
    print("\nMileage Preferences:")
    while True:
        try:
            min_miles = int(input("Enter minimum miles: ").strip())
            if min_miles < 0:
                print("Miles can't be negative")
                continue

            break
        except ValueError:
            print("Please enter a valid number for minimum miles")

    while True:
        try:
            max_miles = int(input(f"Enter maximum miles (must be >= {min_miles}): ").strip())
            if max_miles < min_miles:
                print("Maximum must be greater than or equal to minimum.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for maximum miles")
    
    return (min_miles, max_miles)