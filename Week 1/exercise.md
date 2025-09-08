
## 🔹 1. Create & Move Files

```bash
# Create a new directory
mkdir myproject

# Navigate into it
cd myproject

# Create some files
touch file1.txt file2.txt

# Move file1.txt into a subdirectory
mkdir backup
mv file1.txt backup/
```

✅ Now `file1.txt` is inside `backup/` and `file2.txt` is still in `myproject/`.

---

## 🔹 2. Change File Permissions

```bash
# Give the owner read, write, and execute permissions
chmod 700 file2.txt

# Make file2.txt readable by everyone
chmod 644 file2.txt

# Check permissions
ls -l
```

👉 Output might look like:

```
-rw-r--r-- 1 user user   0 Sep  8 12:00 file2.txt
```

---

## 🔹 3. Pipe Commands

```bash
# Show running processes
ps aux

# Pipe into grep to search for python processes
ps aux | grep python

# Pipe into less for scrolling view
ps aux | less
```

✅ This way, you can filter or navigate large outputs.

---

⚡Pro tip: combine them! Example:

```bash
ls -l | grep ".txt"
```

→ Lists only `.txt` files in the directory.
