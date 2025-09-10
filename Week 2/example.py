# x = 10

# def outer():
#     x = 20
#     def inner():
#         nonlocal x  # refers to outer()'s x
#         x = 30

#         print("inner:", x)
#     inner()
#     print("outer:", x)

# outer()
# print("global:", x)

# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#     spam = "test spam" # local variable
#     do_local()
#     print(spam)
#     do_nonlocal()
#     print(spam)
#     do_global()
#     print(spam)
# scope_test()
# print(spam)


# x = 10  # global 
# def f1():
#     x = 20
#     print(x)
    
# f1()
# print(x)

# x = 10  # global 
# def f1():
#     global x
#     x = 20
#     print(x)
    
# f1()
# print(x)# for modify the local variable

# class complex:
#     def __init__(self, realpart, imagepart):
#         self.i = imagepart
#         self.r = realpart
# x = complex(3.0,-4.5)
# print(x.r,x.i)

# class myclass():
#     pass

# x = myclass()
# x.counter = 1

# while x.counter < 10:
#     x.counter = x.counter * 2

# print(x.counter)

# class dog:
#     kind = 'canine'

#     def __init__(self, name):
#         self.name = name
# d = dog('x')
# e = dog('y')
# print(d.kind)
# print(d.name)
# print(e.name)


# # 📌 Example: Class Method for Tracking Objects

# class example:
#     count = 0
    
#     def __init__(self,name):
#         self.name = name
#         example.increment_count()
#     @classmethod
#     def increment_count(cls):
#         cls.count +=1
    
#     @classmethod
#     def get_counts(cls):
#         return cls.count

# a = example("first")
# b = example("second")
# c = example("third")

# print(example.get_counts())

#  # 📌 Example: Static Method for Tracking Objects
# class example:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         example.increment_count()

#     @staticmethod
#     def increment_count():
#         example.count +=1
    
#     @staticmethod
#     def get_count():
#         return example.count
    
# a = example("x")
# b = example("y")

# print(example.get_count())
        
# class dog:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return f"{self.name} says woof"
#     def birthday(self):
#         return f"Happy Birthday, {self.name}! you are now {self.age} years old"
    
# dog1 = dog("x",3)
# dog2 = dog("y", 4)
# dog3 = dog("z", 4)

# print(dog1.name, dog1.age)
# print(dog2.name, dog2.age)
# print(dog3.name, dog3.age)

