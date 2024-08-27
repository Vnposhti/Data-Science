import datetime
import math
class cars:
    confirmation_time=''
    def __init__(self,available_cars):
        self.available_cars=available_cars
    def display_cars(self):
        print('Available no. of cars : ',self.available_cars)
    def duration(self,rental_mode,confirmation_time):
        rental_mode_list=['HOURLY','DAILY','WEEKLY']
        current_time=datetime.datetime.now()
        if (rental_mode.upper()) not in rental_mode_list:
            print('Invalid rental mode')
            return
        if rental_mode.upper()=='HOURLY':
            rental_time=math.ceil((current_time-confirmation_time).total_seconds()/3600)
        if rental_mode.upper()=='DAILY':
            rental_time=math.ceil((current_time-confirmation_time).days)+1
        if rental_mode.upper()=='WEEKLY':
            rental_time=math.ceil((current_time-confirmation_time).days/7)
        return rental_time
    def rent_car(self,no_of_cars,rental_mode,req_time):
        if(no_of_cars>0 and no_of_cars<=self.available_cars):
            self.available_cars=self.available_cars-no_of_cars
            cars.confirmation_time=req_time
            print('Thank you. You have rented {} cars on {} basis',no_of_cars,rental_mode)
        else:
            print('Not enough cars available. Try after some time')
    def bill(self,no_of_cars,rental_mode):
        a=self.duration(rental_mode,cars.confirmation_time)
        self.available_cars=self.available_cars+no_of_cars
        if rental_mode.upper()=='HOURLY':
            rental_price=a*no_of_cars*50
        if rental_mode.upper()=='DAILY':
            rental_price=a*no_of_cars*1000
        if rental_mode.upper()=='WEEKLY':
            rental_price=a*no_of_cars*5000
        print('Time of Order : ',cars.confirmation_time)
        print('Time of Return : ',datetime.datetime.now())
        print('Time Duration : ', a)
        print('Rental mode : ',rental_mode)
        print('No. of cars on rent : ',no_of_cars)
        print('Total rent : ', rental_price)