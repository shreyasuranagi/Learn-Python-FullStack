#single level

class Vehicle:
    fuel_type='petrol'
    company='hero'


class Bike(Vehicle):
    wheels=2
    passengers=2
    mileage=60

    def __init__(self,model,fuel):
        self.model=model
        self.fuel_type=fuel

b=Bike('honda','diesel')
print(b.__dict__)
print(b.company)
print(b.fuel_type)
print(b.fuel_type)
print(Vehicle.fuel_type)
print(Vehicle.passengers)
    
    


        
    
