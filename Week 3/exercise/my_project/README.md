## 1️⃣ Install Poetry

If you don’t have Poetry installed yet:

```bash
# Linux / macOS
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Check installation:

```bash
poetry --version
```

---

## 2️⃣ Create a New Project

```bash
poetry new my_project
```

This creates the following structure:

```
my_project/
├── pyproject.toml
├── README.rst
├── my_project/
│   └── __init__.py
└── tests/
    └── __init__.py
```

* **`pyproject.toml`** – where dependencies and project metadata are declared.

---

## 3️⃣ Add Dependencies

Example: add `requests` library:

```bash
poetry add requests
```

* This updates `pyproject.toml` and generates a **`poetry.lock`** file for reproducible installs.

---

## 4️⃣ Activate Poetry’s Virtual Environment

```bash
poetry shell
```

* This activates an **isolated virtual environment** for the project.
* All packages installed via Poetry go into this environment.

Check Python and pip paths:

```bash
which python
which pip
```

(On Windows, use `where python`)

---

## 5️⃣ Run Your Project

Suppose you have `my_project/main.py`:

```python
# my_project/main.py
import requests

print(requests.__version__)
```

Run it inside the Poetry environment:

```bash
python my_project/main.py
```

---

## 6️⃣ Install Dependencies (if project cloned)

If you cloned a project with a `pyproject.toml`:

```bash
poetry install
poetry shell
```

Here’s how to handle it:

---

## 1️⃣ Activate the Virtual Environment (Poetry 2.x)

### Option A: Recommended – `poetry env activate`

1. First, check which virtual environment Poetry created:

```bash
poetry env list
```

You’ll see something like:

```
my_project-py3.11 (Activated)
```

2. Activate it:

```bash
poetry env activate python3.11
```

* Replace `python3.11` with the environment name shown in the list.
* This activates the venv in your current shell session.

---

### Option B: Use the `shell` plugin (optional)

If you really want `poetry shell` like in 1.x:

```bash
poetry self add poetry-plugin-shell
poetry shell
```

* This installs the shell plugin and restores the old behavior.

---

## 2️⃣ Run Python Inside the Poetry Environment

Once the environment is active:

```bash
python my_project/main.py
```

Or, without activating, you can run scripts directly:

```bash
poetry run python my_project/main.py
```

* `poetry run` executes commands inside the project’s virtual environment without activating it manually.

---

✅ **Summary of New Poetry 2.x Workflow:**

| Action                    | Command                                                |
| ------------------------- | ------------------------------------------------------ |
| List virtual environments | `poetry env list`                                      |
| Activate environment      | `poetry env activate <env_name>`                       |
| Run a command in venv     | `poetry run <command>`                                 |
| Optional: restore shell   | `poetry self add poetry-plugin-shell` + `poetry shell` |


* This installs all dependencies listed in the lockfile and activates the venv.

---

✅ **Summary:**

1. Install Poetry
2. `poetry new my_project`
3. Add dependencies with `poetry add`
4. Activate environment with `poetry shell`
5. Run your Python scripts inside the environment

---
