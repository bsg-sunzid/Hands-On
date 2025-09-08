## 🔹 1. System Info

```bash
free -h
```

👉 See free memory in human-readable format.

---

## 🔹 2. File System Navigation

```bash
pwd
ls -l
cd /tmp
pwd
cd -
```

👉 Try moving between directories, then return to the previous one.

---

## 🔹 3. File & Directory Operations

```bash
mkdir practice_dir
cd practice_dir
touch file1.txt file2.txt
ls
cp file1.txt copy_file1.txt
mv file2.txt renamed_file2.txt
```

👉 Create, copy, and rename files.

---

## 🔹 4. Wildcards

```bash
touch a.txt b.txt c.log d.log
ls *.txt
ls ?.log
```

👉 Use `*` and `?` to match files.

---

## 🔹 5. Viewing Files

```bash
echo "Line1" > sample.txt
echo "Line2" >> sample.txt
cat sample.txt
head -n 1 sample.txt
tail -n 1 sample.txt
```

👉 Compare outputs of `cat`, `head`, `tail`.

---

## 🔹 6. Permissions

```bash
ls -l
chmod 755 sample.txt
ls -l sample.txt
```

👉 Change file permissions and inspect.

---

## 🔹 7. Processes

```bash
ps aux | head -5
sleep 60 &
ps aux | grep sleep
kill -9 <PID>
```

👉 Start a background process (`sleep`), find it, then kill it.

---

## 🔹 8. Piping & Redirection

```bash
ls -l | grep ".txt"
echo "Hello" > hello.txt
echo "World" >> hello.txt
cat < hello.txt
```

👉 Practice piping and redirecting input/output.

---

## 🔹 9. Environment Variables

```bash
echo $HOME
export MY_VAR="LinuxPractice"
echo $MY_VAR
```

👉 Set and display environment variables.

---

## 🔹 10. Package Management

(For Debian/Ubuntu)

```bash
sudo apt update
sudo apt install cowsay -y
cowsay "Linux practice is fun!"
```

👉 Install a package and run it.

(For Python)

```bash
pip install requests
pip list | grep requests
pip uninstall requests -y
```

