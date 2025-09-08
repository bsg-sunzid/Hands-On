
# Linux Commands Reference

## System Info
To display the amount of free memory:
```bash
free
````

---

## Working with Directories

* `pwd` → Print name of current working directory
* `cd` → Change directory
* `ls` → List directory contents

### Examples

```bash
[me@linuxbox bin]$ cd /usr
[me@linuxbox usr]$ pwd
/usr
```

Using relative path:

```bash
[me@linuxbox bin]$ cd ..
[me@linuxbox usr]$ pwd
/usr
```

### Special `cd` shortcuts

* `cd` → Changes to your home directory
* `cd -` → Changes to the previous working directory
* `cd ~user` → Changes to user’s home directory (e.g., `cd ~bob`)

---

## File Information

* `file` → Determine file type
* `less` → View file contents

---

## File & Directory Operations

* `cp` → Copy files and directories
* `mv` → Move or rename files and directories
* `mkdir` → Create directories
* `rm` → Remove files and directories
* `ln` → Create hard and symbolic links

---

## Wildcards (Globbing)

* `*` → Matches any characters
* `?` → Matches any single character
* `[chars]` → Matches any character from the set
* `[!chars]` → Matches any character **not** in the set
* `[[:class:]]` → Matches characters in a specific class

### Common Character Classes

* `[:alnum:]` → Alphanumeric
* `[:alpha:]` → Alphabetic
* `[:digit:]` → Digits
* `[:lower:]` → Lowercase letters
* `[:upper:]` → Uppercase letters

---

## `mkdir` – Create Directories

**Usage:**

```bash
mkdir dir1 dir2 dir3
```

Creates three directories: `dir1`, `dir2`, `dir3`.

---

## `cp` – Copy Files

**Usage:**

```bash
cp item1 item2
```

Copy `item1` to `item2`.

```bash
cp item1 item2 dir
```

Copy multiple items into `dir`.

---

## `mv` – Move or Rename Files

**Usage:**

```bash
mv item1 item2
```

Move/rename `item1` to `item2`.

```bash
mv file1 file2 dir1
```

Move `file1` and `file2` into directory `dir1`.

```bash
mv dir1 dir2
```

* If `dir2` doesn’t exist → rename `dir1` → `dir2`
* If `dir2` exists → move `dir1` inside `dir2`

### Examples

```bash
mv file1 file2      # Overwrites file2 if exists
mv -i file1 file2   # Prompts before overwrite
```

---

## `rm` – Remove Files/Directories

**Usage:**

```bash
rm file1            # Delete file1 silently
rm -i file1         # Prompt before deleting file1
rm -r file1 dir1    # Delete recursively
rm -rf file1 dir1   # Force delete, no errors if not found
```

```
