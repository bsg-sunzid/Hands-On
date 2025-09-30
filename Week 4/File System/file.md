
# 📄 Reading and Writing Files in Python

Python provides the `open()` function to work with files. It returns a **file object**, which can be used to read or write data.

---

## 🔹 Basic Syntax

```python
f = open(filename, mode='r', encoding=None)
```

* **filename**: Path to the file.
* **mode**: How the file is opened (default `'r'`).
* **encoding**: Optional; recommended `"utf-8"` for text files.

---

## 🔹 File Modes

| Mode   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| `'r'`  | Read only (default). File must exist.                        |
| `'w'`  | Write only. Creates a new file or **overwrites** existing.   |
| `'a'`  | Append. Writes added to the **end** of file.                 |
| `'r+'` | Read and write. File must exist.                             |
| `'b'`  | Binary mode. Use `'rb'`, `'wb'`, or `'ab'` for binary files. |

> **Note:** Encoding cannot be specified in binary mode.

---

## 🔹 Using `with` (Recommended)

The `with` statement **automatically closes the file**, even if exceptions occur.

```python
with open('workfile', 'w', encoding="utf-8") as f:
    f.write("Hello, World!")

# File is automatically closed
print(f.closed)  # True
```

---

## 🔹 Reading Data

```python
with open('workfile', 'r', encoding="utf-8") as f:
    content = f.read()       # Read entire file
    print(content)
```

* Other methods: `f.readline()` (read a single line), `f.readlines()` (read all lines into a list).

---

## 🔹 Writing Data

```python
with open('workfile', 'a', encoding="utf-8") as f:
    f.write("\nAppending a new line.")
```

* `f.write()` writes a string to the file.
* Always ensure the file is **closed** after writing.

---

## 🔹 Binary Mode Example

```python
with open('image.jpg', 'rb') as f:
    data = f.read()
```

* Use binary mode for **non-text files** like images, PDFs, executables.
* Text mode may **corrupt binary data** due to newline conversions.

---

## 🔹 Without `with`

If you don’t use `with`, you must **manually close** the file:

```python
f = open('workfile', 'r', encoding="utf-8")
data = f.read()
f.close()
```

* Forgetting `f.close()` may result in **incomplete writes** or resource leaks.
* After closing, attempting to read or write raises an error:

```python
f.read()
# ValueError: I/O operation on closed file
```

---

✅ **Key Takeaways:

1. Prefer `with` to handle files automatically.
2. Use the correct **mode** (`'r'`, `'w'`, `'a'`, `'b'`) for your use case.
3. Always **close files** if not using `with`.
4. Use **binary mode** for non-text files.

---


# 📝 Binary File Mode

**Binary mode** is a way of opening files so that Python reads or writes the **raw bytes** directly, without any encoding or newline transformations.

---

### 🔹 Key Differences from Text Mode

| Feature          | Text Mode (`'r'`, `'w'`, `'a'`)                 | Binary Mode (`'rb'`, `'wb'`, `'ab'`)               |
| ---------------- | ----------------------------------------------- | -------------------------------------------------- |
| Data type        | Strings (`str`)                                 | Bytes (`bytes`)                                    |
| Encoding         | Encodes/decodes automatically (e.g., UTF-8)     | No encoding/decoding                               |
| Newline handling | Converts `\n` to platform-specific line endings | No newline conversion                              |
| Use case         | Text files (CSV, TXT, JSON)                     | Non-text files (images, videos, PDFs, executables) |

---

### 🔹 Why Use Binary Mode?

1. **Preserve raw data:** Text mode may alter bytes (e.g., newline conversion), which can corrupt non-text files.
2. **Exact copy of data:** Needed when working with files like `.jpg`, `.png`, `.exe`, `.pdf`, etc.
3. **Reading/writing bytes directly:** Sometimes you need to manipulate the file at the byte level.

---

### 🔹 Examples

#### Writing a binary file

```python
data = b"Hello, binary world!"  # bytes literal
with open("example.bin", "wb") as f:
    f.write(data)
```

#### Reading a binary file

```python
with open("example.bin", "rb") as f:
    content = f.read()
print(content)  # b'Hello, binary world!'
```

* Notice the **b prefix** (`b"..."`) for bytes.
* No encoding is applied; the file is read/written exactly as-is.

---

✅ **Summary:**
Binary mode means Python works with **raw bytes** instead of strings.
It’s essential for **non-text files** or when exact byte preservation is required.

---