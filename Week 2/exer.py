class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print("this vehicle is moving.")

class car (Vehicle):
    def drive(self):
        print(f"the car {self.brand} is driving")
class bike(Vehicle):
    def drive(self):
        print(f"the bike {self.brand} is moving")

Vehicles = [car("toyota"), bike("honda"),car("tesla")]
for v in Vehicles:
    v.drive()