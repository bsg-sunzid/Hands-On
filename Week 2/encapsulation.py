# public attributes --- all attributes are public accessible from anywhere

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = student("Alice",20)
print(s.name)
print(s.age)

# protected attributes --- denoted by single leading underscore "_attribute"
# this is for the internal not the external
# accessible from outside but cannot modify it directly

class student:
    def __init__(self,name ,age):
        self._age = age # protected attributes
    def get_age(self):
        return self._age
s = student("bob",2)
print(s._age)    # accessible but discourged 
print(s.get_age()) # preferred only

# private attributes 
# denoted by double underscore __attributes
# makes it harder but not impossible to access from outside

class student:
    def __init__(self, name, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
s = student("bb",39)
# print(s.__marks)

print(s.get_marks())