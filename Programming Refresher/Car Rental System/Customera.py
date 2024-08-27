import datetime
from CarRental import cars 
class customers:
    rental_mode=''
    def __init__(self):
        pass
    def request_car(self, car_obj):
        no_of_cars = int(input("How many cars would you like to rent ?"))
        if (no_of_cars>0):
            customers.rental_mode = input("How would you like to rent car - Hourly/Daily/Weekly ?")
            car_obj.rent_car(no_of_cars,customers.rental_mode,datetime.datetime.now())
        else:
            print('Enter valid Number of cars.')
    def return_car(self, car_obj):
        no_of_cars = int(input("How many cars would you like to return ?"))
        car_obj.bill(no_of_cars,customers.rental_mode)