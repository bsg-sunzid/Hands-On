# 🐍 OOP Fundamentals in Python

## 1. Classes and Objects
- **Class** → A blueprint for creating objects.  
- **Object (Instance)** → A concrete entity created from a class.  
- Each object has **attributes** (data) and **methods** (behavior).

Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

buddy = Dog("Buddy")   # object (instance)
````

---

## 2. Attributes and Methods

* **Attributes** → Variables that belong to an object.
* **Methods** → Functions defined inside a class, describe the object’s behavior.

Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name   # attribute

    def bark(self):        # method
        return f"{self.name} says woof!"
```

---

## 3. Types of Methods

Python supports **3 kinds of methods** inside classes:

### a) Instance Methods

* Most common type.
* Take `self` as the first parameter.
* Operate on **instance attributes** (unique to each object).

```python
class Example:
    def instance_method(self):
        return "I work on instance data"
```

### b) Class Methods

* Use the `@classmethod` decorator.
* Take `cls` (class itself) as the first parameter.
* Often used for **factory methods** or class-level operations.

```python
class Example:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1
```

### c) Static Methods

* Use the `@staticmethod` decorator.
* Take **no `self` or `cls` parameter**.
* Behave like regular functions but live inside the class for organization.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

---

## ✅ Quick Recap

* **Classes** define blueprints; **objects** are instances.
* **Attributes** = data, **Methods** = behavior.
* **Instance methods** → work with object data (`self`).
* **Class methods** → work with class-level data (`cls`).
* **Static methods** → utility functions inside a class, don’t need `self` or `cls`.
