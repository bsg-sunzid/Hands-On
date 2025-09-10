# ⚙️ Special (Dunder) Methods in Python

Special methods (a.k.a. **dunder methods**, because they start and end with `__`) let you define how objects of a class behave with built-in functions and operators.  
They make your classes more **Pythonic**.

---

## 1️⃣ Initialization & Representation

### `__init__`
- Called when an object is created.
- Used to initialize attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
````

---

### `__str__`

* Called by `print()` or `str(obj)`.
* Meant for **human-readable** representation.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 25)
print(p)   # Alice, 25 years old
```

---

### `__repr__`

* Called by `repr(obj)` or in the interactive shell.
* Meant for **unambiguous representation**, mainly for developers.

```python
class Person:
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

print(repr(p))  # Person(name='Alice', age=25)
```

---

## 2️⃣ Operator Overloading

Python lets you **overload operators** by defining special methods:

* `__add__` → `+`
* `__sub__` → `-`
* `__mul__` → `*`
* `__len__` → `len(obj)`

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        return abs(self.x) + abs(self.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, -1)

print(v1 + v2)   # Vector(6, 2)
print(len(v1))   # 5
```

---

## 3️⃣ Iteration Protocol (`__iter__`)

Makes an object iterable.

```python
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

for num in CountDown(3):
    print(num)  
# 3, 2, 1
```

---

## 4️⃣ Callable Objects (`__call__`)

Allows an object to be called like a function.

```python
class Greeter:
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        return f"Hello, {self.name}!"

g = Greeter("Alice")
print(g())  # Hello, Alice!
```

---

## 5️⃣ Context Managers (`__enter__`, `__exit__`)

Used with `with` statements to manage resources.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello world!")
# File auto-closed
```

---

# ✅ Summary

* `__init__`: Object creation & initialization.
* `__str__`, `__repr__`: Human-readable vs developer-friendly representation.
* Operator overloading (`__add__`, `__len__`, etc.).
* `__iter__`: Make objects iterable.
* `__call__`: Make objects behave like functions.
* `__enter__` / `__exit__`: Context manager support.
* `__enter__` = setup (open resource).
* `__exit__` = cleanup (close resource).