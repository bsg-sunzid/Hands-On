# class person(object):
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def display(self):
#         print(self.name, self.id)

# emp = person("elon",102)
# emp.display()

# class emp(person):
#     def Print(self):
#         print("emp class is created")
# emp_details = emp("xyz", 30)
# emp_details.display()
# emp_details.Print()

# class person:
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
    
#     def display(self):
#         print(self.name, self.idnumber)

# class employee(person):
#     def __init__(self, name, idnumber, salary):
#         super().__init__(name, idnumber)
#         self.salary = salary
#     def display_emp(self):
#         super().display()
#         print(self.salary)
    
# emp = employee("bob",300,300000)
# emp.display_emp()

# single inheritance

# class Animal:
#     def speak(self):
#         print("This animal makes a sound")
# class Dog(Animal):
#     def speack(self):
#         return super().speak()
    
# dog = Dog()
# dog.speak()

# # multilevel
# class animal:
#     def eat(self):
#         print("eating...")
# class mammal(animal):
#     def walk(self):
#         print("walking...")
# class dog(mammal):
#     def bark(self):
#         print("barking...")

# d = dog()
# d.bark()
# d.eat()

# # multiple 
# class goat(dog,mammal):
#     def sound(self):
#         print("sounding...")

# x = goat()
# x.sound()

# # 5. Hybrid Inheritance (Multiple + Multilevel)
# class ok(goat, animal):
#     def foo(self):
#         print("fooing...")

# y = ok()
# y.foo()

