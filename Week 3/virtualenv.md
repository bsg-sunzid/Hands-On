
# 📦 Package & Environment Management

Python projects often need their **own versions of libraries**.
Using a virtual environment prevents conflicts between projects.

---

## 🔹 `venv` – Built-in Virtual Environments

`venv` is a **standard library module** (no installation required, Python ≥ 3.3).

It lets you create **isolated environments** where each has its **own interpreter** and **own `site-packages` folder** (installed libraries).
This keeps dependencies for different projects separate.

---

### 🚀 Quick Start

```bash
# create a virtual environment called .venv
python3 -m venv .venv

# activate it (Linux/Mac)
source .venv/bin/activate

# activate it (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
```

To leave the environment:

```bash
deactivate
```

---

### ⚙️ What `venv` Does Internally

1️⃣ **Creates the environment directory**

* Makes the directory you name (e.g. `myenv`), creating parents if needed.
* Adds a small config file: `pyvenv.cfg` (records the “home” Python installation).

2️⃣ **Sets up the Python executable**

* Creates `bin/` (Linux/Mac) or `Scripts\` (Windows) containing copies or symlinks of the Python executable and activation scripts.
* Activation scripts (`activate`, `activate.csh`, `activate.ps1`, etc.) change your shell environment to use the venv.

3️⃣ **Prepares the `site-packages` area**

* Creates `lib/pythonX.Y/site-packages/` (Linux/Mac) or `Lib\site-packages\` (Windows).
* Pip installs packages here when you’re inside the venv.

4️⃣ **Reuses existing directory if specified**

* Running `python -m venv existingdir` reuses the directory rather than failing.

---

### 🗂 Typical Folder Structure

```text
myenv/
├── bin/
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── python   -> the Python interpreter (copy or symlink)
│   └── pip      -> pip inside the venv
├── include/
│   └── ...
├── lib/
│   └── python3.X/
│       └── site-packages/
│           └── ... (installed packages go here)
└── pyvenv.cfg
```

---

## 🔹 `venv` vs `virtualenv`

| Feature               | `venv` (built-in)               | `virtualenv` (third-party)                     |
| --------------------- | ------------------------------- | ---------------------------------------------- |
| Where it comes from   | Standard library (Python ≥ 3.3) | Install via `pip install virtualenv`           |
| Speed                 | Normal                          | Often faster, especially on Windows            |
| Cross-version support | Uses the Python you run it with | Can create envs for other Python versions      |
| Extra features        | Basic                           | More options: seed pip, upgrade, relocate envs |

---

With either tool, you get **isolated Python environments** and can manage packages per project cleanly.

