
# ⚠️ Exceptions in Python

Even if a statement is **syntactically correct**, it may cause an **error during execution**.
Such errors are called **exceptions**.

* Unlike syntax errors, exceptions occur **while the program runs**.
* Exceptions **do not have to be fatal**; Python provides ways to handle them using `try` / `except`.

---

### 🔹 Examples of Exceptions

```python
10 * (1/0)
```

Output:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
ZeroDivisionError: division by zero
```

---

```python
4 + spam*3
```

Output:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
NameError: name 'spam' is not defined
```

---

```python
'2' + 2
```

Output:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
TypeError: can only concatenate str (not "int") to str
```

---

### 🔹 Understanding the Error Message

1. **Traceback**

   * Shows the **call stack** where the error occurred.
   * Lists the file and line number causing the exception.

2. **Exception Type**

   * Example: `ZeroDivisionError`, `NameError`, `TypeError`.
   * Built-in exceptions are **identifiers**, not keywords.

3. **Exception Message**

   * Describes **why the error happened**.
   * Example: `"division by zero"` or `"can only concatenate str (not 'int') to str"`.

---

### 🔹 Common Built-in Exceptions

| Exception Type      | Meaning                                |
| ------------------- | -------------------------------------- |
| `ZeroDivisionError` | Division or modulo by zero             |
| `NameError`         | Name not defined in local/global scope |
| `TypeError`         | Operation applied to an incorrect type |
| `ValueError`        | Wrong value type for an operation      |
| `IndexError`        | Sequence index out of range            |
| `KeyError`          | Dictionary key not found               |
| `FileNotFoundError` | File operation failed (file not found) |

> There are many other built-in exceptions.
> Python also allows **user-defined exceptions** by subclassing `Exception`.

---

### 🔹 Key Points

* Exceptions **happen at runtime**, not during parsing.
* The **last line** of the traceback tells you the **exception type and message**.
* Python provides **mechanisms to handle exceptions** so that your program can continue running instead of crashing.


# 🛠️ Handling Exceptions in Python

Python allows you to **handle runtime errors** (exceptions) gracefully using the `try` … `except` statement.
This prevents the program from crashing and lets you respond to errors appropriately.

---

## 🔹 Basic Syntax

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
```

**How it works:**

1. **Try Clause**

   * The code inside `try` is executed first.
   * If no exception occurs, the `except` clause is skipped.

2. **Except Clause**

   * Executed only if an exception of the specified type occurs.
   * If a different exception occurs, it propagates to outer `try` statements or terminates the program.

---

## 🔹 Handling Multiple Exceptions

```python
try:
    # some code
except (RuntimeError, TypeError, NameError):
    # handle multiple exceptions
    pass
```

* You can catch multiple exceptions using a **tuple**.
* Only **one except clause** is executed per exception.

---

## 🔹 Exception Class Hierarchy

* Exceptions are **classes**, derived from `BaseException`.
* `Exception` is the base class for most non-fatal exceptions.
* Subclasses can be caught individually:

```python
class B(Exception): pass
class C(B): pass
class D(C): pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

> **Tip:** Order matters. The first matching `except` is executed.

---

## 🔹 Accessing Exception Arguments

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # <class 'Exception'>
    print(inst.args)     # ('spam', 'eggs')
    print(inst)          # ('spam', 'eggs')
    x, y = inst.args     # unpack arguments
    print('x =', x)
    print('y =', y)
```

* `.args` stores arguments passed to the exception.
* `__str__()` prints the arguments in error messages.

---

## 🔹 Catching Almost All Exceptions

```python
try:
    f = open('myfile.txt')
    i = int(f.readline().strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise  # re-raise the exception
```

* Use `Exception` as a wildcard to catch unexpected exceptions, but prefer **specific exceptions**.

---

## 🔹 Optional `else` Clause

* Executes code **only if no exception occurred** in `try`.

```python
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('Cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

> `else` avoids accidentally catching exceptions from unrelated code.

---

## 🔹 Exceptions in Functions

```python
def this_fails():
    x = 1 / 0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
```

* Exceptions in functions called from a `try` block are also caught.

---

## ✅ Summary

* **`try`**: block of code to monitor for exceptions
* **`except`**: block to handle specific exceptions
* **`else`**: runs if no exceptions occur
* **`finally`** (optional, not shown above): always runs, useful for cleanup
* Catch **specific exceptions** when possible; use `Exception` as a fallback


# 🛑 Raising Exceptions in Python

Python allows programmers to **force an exception** using the `raise` statement.
This is useful when you want to signal that an error condition has occurred.

---

### 🔹 Raising a Specific Exception

```python
raise NameError('HiThere')
```

Output:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

* The argument to `raise` can be:

  * **An exception instance**: `raise NameError('HiThere')`
  * **An exception class**: `raise ValueError` (Python automatically calls the constructor: `ValueError()`)

---

### 🔹 Re-raising an Exception

If you catch an exception but want to propagate it further:

```python
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
```

Output:

```
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

* `raise` without arguments **re-raises the last caught exception**.
* Useful for logging or adding additional context before letting the exception continue.

---

### 🔹 Key Points

* `raise` is used to **signal an error condition** manually.
* You can raise **built-in exceptions** (like `ValueError`, `NameError`) or **custom exceptions** (subclass of `Exception`).
* Re-raising allows the exception to propagate **after optional handling**.



# 📝 Logging vs Re-raising Exceptions

When handling exceptions, you often have two main options: **log the error** or **re-raise the exception** (or both). Understanding the difference is important for building maintainable code.

---

## 🔹 1️⃣ Logging an Exception

**Logging** means recording the exception details (message, type, stack trace) **without stopping the program**.

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    x = int("abc")
except ValueError as e:
    logging.error("Conversion failed", exc_info=True)
```

Output:

```
ERROR:root:Conversion failed
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
```

* `exc_info=True` includes the full traceback.
* The program **continues running** after logging.
* Useful for **monitoring errors** in production or debugging.

---

## 🔹 2️⃣ Re-raising an Exception

**Re-raising** passes the exception up to the caller after optionally handling it.

Example:

```python
try:
    x = int("abc")
except ValueError as e:
    print("Caught ValueError, but re-raising...")
    raise
```

Output:

```
Caught ValueError, but re-raising...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
```

* The exception propagates after executing the `except` block.
* Useful when you **cannot fully handle the exception locally**, but want to log or perform cleanup first.

---

## 🔹 3️⃣ Combined Approach

Often, you **log the exception** and then **re-raise it** so that it is still handled upstream:

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    x = int("abc")
except ValueError as e:
    logging.error("Conversion failed", exc_info=True)
    raise
```

* This logs the error **and still propagates it** to be handled by higher-level code.

---

### 🔹 Summary Table

| Action             | Behavior                                                 | Use Case                                                  |
| ------------------ | -------------------------------------------------------- | --------------------------------------------------------- |
| **Log**            | Record the exception details, program continues          | Monitoring, debugging, non-fatal errors                   |
| **Re-raise**       | Pass the exception to outer scope, may terminate program | When you cannot handle it locally, want upstream handling |
| **Log + Re-raise** | Record details and propagate exception                   | Best practice in many production systems                  |

---

✅ **Key Takeaway:**

* Use **logging** to track errors.
* Use **re-raising** to let the exception propagate.
* Combining both is often the best approach in larger applications.


# 🛠️ Custom Exceptions in Python

Python raises exceptions to signal **errors that occur during program execution**. While built-in exceptions handle many cases, **custom exceptions** allow you to define your own, application-specific error types.

---

## 🔹 Why Define Custom Exceptions?

* **Clarity:** Provide clear, specific error messages relevant to your application.
* **Granularity:** Enable fine-grained error handling to pinpoint issues.
* **Reusability:** Can be reused across different modules or projects.

---

## 1️⃣ Defining a Basic Custom Exception

```python
class MyCustomError(Exception):
    """Exception raised for custom error scenarios."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```

* Inherits from Python’s built-in `Exception` class.
* Can store additional attributes like `message` for context.

---

## 2️⃣ Defining a Custom Exception with Extra Attributes

```python
class MyCustomError(Exception):
    """Exception raised for specific application errors."""
    
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
```

* Stores extra information (`error_code`) for more context.
* Overrides `__str__()` to provide a readable string representation.

---

## 3️⃣ Raising a Custom Exception

```python
def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    return a / b
```

* Use the `raise` keyword followed by your exception instance.
* The program signals an error condition when the exception is raised.

---

## 4️⃣ Handling Custom Exceptions

```python
try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Caught an error: {e}")
```

* Custom exceptions are handled the same way as built-in exceptions.
* Access attributes (like `error_code`) to get more information.

---

## 5️⃣ Advanced Example: File Processing Error

```python
class FileProcessingError(Exception):
    def __init__(self, message, filename, lineno):
        super().__init__(message)
        self.message = message
        self.filename = filename
        self.lineno = lineno

    def __str__(self):
        return f"{self.message} in {self.filename} at line {self.lineno}"


try:
    raise FileProcessingError("Syntax error", "example.txt", 13)
except FileProcessingError as e:
    print(f"Caught an error: {e}")
```

* Useful for giving detailed error context (filename, line number, etc.).

---

## 🔹 Tips for Effective Custom Exceptions

1. **Naming:** Use clear names ending with `Error` to indicate exceptions.
2. **Documentation:** Include docstrings explaining when to use the exception.
3. **Hierarchy:** Consider creating an exception hierarchy for complex applications.

   ```python
   class AppError(Exception): pass
   class DatabaseError(AppError): pass
   class ValidationError(AppError): pass
   ```

---

✅ **Summary:**
Custom exceptions provide **clarity, context, and control** over error handling in your Python programs. Use them to make your code **more readable, maintainable, and robust**.
