

# 🛑 Syntax Errors in Python

**Syntax errors**, also called **parsing errors**, occur when the Python parser **cannot understand your code** because it violates the language rules.

These are among the most common errors for beginners.

---

### Example

```python
while True print('Hello world')
```

Output:

```
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

---

### 🔹 How Python Reports Syntax Errors

1. **Displays the offending line**

   * Shows the line where it first detected a problem.

2. **Uses arrows to highlight the error**

   * In the example, the arrow points at `print('Hello world')`.

3. **Shows file name and line number**

   * Example: `<stdin>, line 1` (or the actual filename if running a script).

> ⚠️ Note: The arrow **does not always point to the exact cause**.
> In this example, the actual problem is a **missing colon (`:`)** after `while True`.

Corrected code:

```python
while True:
    print('Hello world')
```

---

### 🔹 Tips to Avoid Syntax Errors

* Always check for **missing colons** after `if`, `for`, `while`, `def`, and `class` statements.
* Ensure **proper indentation** (Python relies on it).
* Watch for **unmatched parentheses, brackets, or quotes**.
* Read the **error message carefully**—it tells you the line and approximate location of the problem.

---

✅ **Summary:**
Syntax errors happen when your code **breaks Python’s grammar rules**.
The interpreter points you to the line and position where it got confused, but you may need to look **just before** that spot to find the actual mistake.
