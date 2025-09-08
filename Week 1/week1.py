"""
Python Fundamentals Refresher
Covers:
- Variables, operators, expressions
- Control flow (if, loops, functions)
- Core data structures (list, tuple, dict, set)
- String manipulation
- Collections module (stack, queue, deque)
"""

# -------------------------------
# 1. Variables, Operators, Expressions
# -------------------------------

x = 10
y = 3
sum_value = x + y
product = x * y
power = x ** y

print (f"Sum: {sum_value}, Prodcut: {product}, Power: {power}")

# -------------------------------
# 2. Control Flow: if, loops, functions
# -------------------------------

def check_number(n):
    if n>0:
        return "positive"
    elif n == 0:
        return "zero"
    else:
        return "negative"

for i in range(-1,2): 
    print(f"{i} is {check_number(i)}")  

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(f"Factorial of 5: {factorial(5)}")


words = ['sunzid','sun','sunzi','sunzidul']
for i in range(len(words)):
    print(i,words[i])

from collections import Counter
freq = Counter(words)
print(freq)

for w in words:
    print(f"{w}:{len(w)}")

words.reverse()
print(words)

text = "sunzid"
reversed_text = "".join(reversed(text))
print(reversed_text)

reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text
print(reversed_text)

# Lists
fruits = ["apple","banana"]
fruits.append("date")
print("List:", fruits)

# Tuple
coordinates = (10,20)
print("Tuple:", coordinates)

# Dictionary
student = {"name": "Alice", "age": 22}
student["grade"]="A"
print(student)

# set
numbers = {1,2,3,4,2,3}
print(numbers)

# string manipulation

text = "Python Basics"
print("Original:", repr(text))
print("lowercase:",text.lower())
print("uppercase:",text.upper())
print("strip:",text.strip())
print("Replace:", text.replace("Basics","Fundamentals"))
print("Split:",text.split())
print("Join", "-".join(["Learn","Python"]))


# -------------------------------
# 5. Collections Module
# -------------------------------

from collections import deque

stack =[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("stack (LIFO):", stack)
stack.pop()
print("stack (pop):", stack)
stack.pop(1)
print("stack (pop1):", stack)

# Queue using deque
queue = deque()
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print("Queue", queue)
queue.popleft()
print("pop", queue)

d = deque([1,2,3])
d.appendleft(0)
d.append(4)
print(d)