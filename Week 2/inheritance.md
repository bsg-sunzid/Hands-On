# 🐍 Inheritance and `super()` in Python

## 🔹 What is `super()`?

The **`super()` function** is used in **inheritance** when a child class wants to access methods or attributes from its **parent class** without directly naming it.

👉 Most often, it’s used inside the `__init__()` method to **initialize parent attributes**.

```python
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

class Employee(Person):
    def __init__(self, name, idnumber, salary):
        super().__init__(name, idnumber)  # call parent constructor
        self.salary = salary
```

---

## ✅ Why Use `super()`?

* **Code Reuse** → No need to rewrite parent’s initialization code.
* **Maintainability** → If the parent’s constructor changes, child classes don’t break.
* **Multiple Inheritance** → Works better than calling parent class directly (`Parent.__init__`) since `super()` follows Python’s **Method Resolution Order (MRO)**.

---

## 🔹 Types of Inheritance in Python

### 1️⃣ Single Inheritance

A child class inherits from **one parent class**.

```python
class Animal:
    def sound(self):
        print("Generic Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

dog = Dog()
dog.sound()  # Woof!
```

---

### 2️⃣ Multiple Inheritance

A child class inherits from **more than one parent class**.

```python
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    def sound(self):
        print("Quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.sound()
```

---

### 3️⃣ Multilevel Inheritance

A class is derived from another class, which is itself derived from another class.

```python
class Animal:
    def eat(self):
        print("Eating...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Dog(Mammal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()   # from Animal
dog.walk()  # from Mammal
dog.bark()  # from Dog
```

---

### 4️⃣ Hierarchical Inheritance

Multiple classes inherit from the **same parent class**.

```python
class Animal:
    def sound(self):
        print("Generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()
dog.sound()  # Woof!
cat.sound()  # Meow!
```

---

### 5️⃣ Hybrid Inheritance

A combination of more than one type of inheritance.

```python
class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

class C(A):
    def method_C(self):
        print("Method C")

class D(B, C):  # Hybrid (Multiple + Hierarchical)
    def method_D(self):
        print("Method D")

obj = D()
obj.method_A()
```

---

## 🔹 Method Resolution Order (MRO)

When using multiple inheritance, Python follows a **specific order** to decide which class method to call.
This order can be seen using:

```python
print(D.__mro__)
# or
help(D)
```

---

## ✅ Summary

* `super()` is used to access parent methods/attributes efficiently.
* Python supports **single, multiple, multilevel, hierarchical, and hybrid inheritance**.
* MRO ensures predictable behavior in multiple inheritance.


# 🔄 Method Overriding in Python

## 🔹 What is Method Overriding?

* **Method overriding** occurs when a **child class defines a method with the same name as a method in its parent class**.
* The **child’s method replaces (overrides)** the parent’s method when called from the child object.
* This is a key feature of **polymorphism** in OOP.

---

## 🔹 Example: Simple Method Overriding

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):   # overriding parent method
        print("Woof! Woof!")

# --- Usage ---
a = Animal()
a.sound()   # Some generic animal sound

d = Dog()
d.sound()   # Woof! Woof!
```

✅ Here, the `Dog` class overrides the `sound()` method of `Animal`.

---

## 🔹 Using `super()` with Overriding

Sometimes you want to **extend** the parent method instead of completely replacing it.
Use `super()` to call the parent’s method inside the child’s override.

```python
class Person:
    def introduce(self):
        print("Hi, I am a person.")

class Employee(Person):
    def introduce(self):
        super().introduce()  # call parent method
        print("I also work as an employee.")

emp = Employee()
emp.introduce()
```

### Output:

```
Hi, I am a person.
I also work as an employee.
```

---

## 🔹 Why Use Method Overriding?

* To **customize behavior** in the child class.
* To **implement polymorphism** (same method name → different behaviors).
* To **reuse parent functionality** and extend it with `super()`.

---

## 🔹 Key Points

* Method overriding only works with **inheritance**.
* The child’s method must have the **same name** as the parent’s method.
* Python decides which method to call based on the **object type**, not the reference type.

---

✅ Example with Polymorphism:

```python
animals = [Dog(), Animal()]

for a in animals:
    a.sound()   # Each object calls its own version
```

👉 Output:

```
Woof! Woof!
Some generic animal sound
```
## 2️⃣ Polymorphism Without Inheritance (Duck Typing)

Python supports **duck typing**:  
👉 *“If it looks like a duck, swims like a duck, and quacks like a duck, then it’s a duck.”*

This means you don’t care about an object’s class; you only care if it has the required method/behavior.

```python
class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I can mimic a duck: Quack!")

# Function doesn’t care about the object’s type
def make_it_quack(thing):
    thing.quack()  

duck = Duck()
person = Person()

make_it_quack(duck)    # Quack! Quack!
make_it_quack(person)  # I can mimic a duck: Quack!
