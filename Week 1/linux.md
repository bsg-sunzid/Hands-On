# Linux Commands Reference

This document covers essential Linux commands with examples, explanations, and usage details.

---

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
* `cat` → Display contents of a file
* `head` → Show the first lines of a file (`head -n 20 file.txt`)
* `tail` → Show the last lines of a file (`tail -f logfile.log` for live monitoring)

---

## File & Directory Operations

* `cp` → Copy files and directories
* `mv` → Move or rename files and directories
* `mkdir` → Create directories
* `rm` → Remove files and directories
* `ln` → Create hard and symbolic links
* `touch` → Create an empty file or update timestamp

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
cp item1 item2        # Copy item1 to item2
cp item1 item2 dir    # Copy multiple items into dir
cp -r dir1 dir2       # Copy directory recursively
```

---

## `mv` – Move or Rename Files

**Usage:**

```bash
mv item1 item2        # Move/rename item1 to item2
mv file1 file2 dir1   # Move file1 and file2 into directory dir1
mv dir1 dir2          # Rename dir1 → dir2 OR move into dir2
```

### Examples

```bash
mv file1 file2        # Overwrites file2 if exists
mv -i file1 file2     # Prompts before overwrite
```

---

## `rm` – Remove Files/Directories

**Usage:**

```bash
rm file1              # Delete file1 silently
rm -i file1           # Prompt before deleting file1
rm -r file1 dir1      # Delete recursively
rm -rf file1 dir1     # Force delete, no errors if not found
```

---

## Permissions

Linux permissions are represented as:

```
-rwxr-xr--
```

* First char → file type (`-` = file, `d` = directory, `l` = link)
* Next 3 → owner permissions (r=read, w=write, x=execute)
* Next 3 → group permissions
* Last 3 → others

### `chmod` – Change permissions

```bash
chmod 755 script.sh   # rwx for owner, rx for group & others
chmod +x script.sh    # Add execute permission
```

### `chown` – Change ownership

```bash
sudo chown user file.txt       # Change owner
sudo chown user:group file.txt # Change owner and group
```

---

## Processes

### `ps` – Show processes

```bash
ps             # Show current shell processes
ps aux         # Show all running processes
ps -ef         # Full-format listing
```

### `kill` – Terminate processes

```bash
kill PID        # Kill process with given PID
kill -9 PID     # Force kill process
```

Find a process:

```bash
ps aux | grep program_name
```

---

## Piping & Redirection

* `|` → Pipe output of one command into another
* `>` → Redirect output (overwrite file)
* `>>` → Append output to file
* `<` → Read input from file

Examples:

```bash
ls -l | grep "txt"        # List files, filter only .txt
echo "hello" > file.txt   # Overwrite file with "hello"
echo "world" >> file.txt  # Append "world" to file
sort < file.txt           # Sort lines from file.txt
```

---

## Environment Variables

### Viewing variables

```bash
printenv           # Show all variables
echo $HOME         # Show HOME directory
echo $PATH         # Show PATH variable
```

### Setting variables

```bash
export VAR=value   # Set variable (temporary)
```

Example:

```bash
export MY_NAME="Alice"
echo $MY_NAME
```

Make permanent → add `export` to `~/.bashrc`.

---

## Installing Packages

### `apt` (Debian/Ubuntu)

```bash
sudo apt update              # Refresh package list
sudo apt install package      # Install package
sudo apt remove package       # Remove package
sudo apt upgrade              # Upgrade all packages
```

### `pip` (Python packages)

```bash
pip install package           # Install package
pip install requests==2.31.0  # Install specific version
pip list                      # List installed packages
pip uninstall package         # Remove package
```

---

# ✅ Summary

This reference covers:

* File system navigation
* File operations
* Permissions
* Processes
* Wildcards
* Piping & redirection
* Environment variables
* Package management