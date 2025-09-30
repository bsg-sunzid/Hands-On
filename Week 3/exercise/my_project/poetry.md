# 📦 Poetry – Dependency Management and Packaging for Python

**Poetry** is a modern Python tool designed for **dependency management, virtual environments, and packaging**. It streamlines the workflow of creating, maintaining, and distributing Python projects.

---

## 🔹 Key Features

1. **Dependency Management**

   * Declare all your project dependencies in **`pyproject.toml`**.
   * Poetry automatically resolves **compatible versions** and installs them.
   * Handles complex dependency trees better than pip alone.

2. **Lockfile for Reproducibility**

   * Generates a **`poetry.lock`** file.
   * Ensures that all installs across machines use the **same versions**, avoiding “works on my machine” issues.

3. **Virtual Environment Management**

   * Poetry can automatically create an isolated **virtual environment** for each project.
   * Keeps project dependencies separate from the system Python.

4. **Packaging and Distribution**

   * Build your project for distribution with `poetry build`.
   * Publish your package to PyPI or a private repository with `poetry publish`.

5. **Cross-Platform**

   * Works on **Linux, macOS, and Windows**.
   * Handles packages that are hard to install with pip, especially on Windows.

6. **Command-line Convenience**

   * `poetry add <package>` → adds a dependency.
   * `poetry remove <package>` → removes a dependency.
   * `poetry install` → installs all dependencies from `pyproject.toml`.
   * `poetry update` → updates dependencies to latest compatible versions.
   * `poetry run <command>` → runs a command inside the virtual environment.

---

## 🔹 Installation

```bash
# Linux / macOS
curl -sSL https://install.python-poetry.org | python3 -

# Windows PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Check installation:

```bash
poetry --version
```

---

## 🔹 Creating a New Project

```bash
poetry new my_project
cd my_project
```

This creates:

```
my_project/
├── pyproject.toml
├── README.rst
├── my_project/
│   └── __init__.py
└── tests/
    └── __init__.py
```

* **`pyproject.toml`** contains project metadata and dependency definitions.

---

## 🔹 Managing Dependencies

### Add a dependency

```bash
poetry add requests
```

### Remove a dependency

```bash
poetry remove requests
```

### Install all dependencies

```bash
poetry install
```

---

## 🔹 Working with Virtual Environments

### List environments

```bash
poetry env list
```

### Activate environment

```bash
poetry env activate <env_name>
```

### Run commands without activating

```bash
poetry run python my_project/main.py
```

### Optional: Restore `poetry shell` behavior

```bash
poetry self add poetry-plugin-shell
poetry shell
```

---

## 🔹 Lockfile and Reproducible Installs

* Poetry generates **`poetry.lock`** after adding dependencies.
* Use it to reproduce the exact same environment:

```bash
poetry install
```

* Export environment to `requirements.txt` if needed:

```bash
poetry export -f requirements.txt --output requirements.txt
```

---

## 🔹 Building and Publishing Packages

```bash
# Build package
poetry build

# Publish to PyPI
poetry publish
```

* Poetry automatically reads metadata from `pyproject.toml` for packaging.

---

## 🔹 Summary

Poetry provides a **modern, reliable, and reproducible** way to:

* Manage dependencies
* Maintain isolated virtual environments
* Build and distribute Python packages

It is often preferred over `venv + pip` for medium to large projects, or when reproducibility and packaging are priorities.

---
