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



class Bookcollection:
    def __init__(self, books):
        self.books = books
    def __len__(self):
        return len(self.books)
    def __str__(self):
        return f"bookcollection with {len(self)} books: {', ' .join(self.books)}"

my_books = Bookcollection(["Python 101", "C++"])
print(len(my_books))
print(my_books)

