
# 📦 Poetry – Python Dependency Management & Packaging

**Poetry** is a modern tool for **dependency management and packaging** in Python.

It simplifies the workflow of managing project libraries and building packages for distribution.

---

### 🔹 Key Features

1. **Dependency Management**

   * Declare your project dependencies in `pyproject.toml`.
   * Poetry automatically resolves and installs compatible versions.

2. **Lockfile for Reproducibility**

   * Generates a `poetry.lock` file to ensure **repeatable installs** across machines.

3. **Environment Isolation**

   * Automatically creates a virtual environment for your project.

4. **Packaging & Distribution**

   * Build your project into a distributable package:

   ```bash
   poetry build
   ```

   * Publish to PyPI:

   ```bash
   poetry publish
   ```

5. **Easy Project Management**

   * Add dependencies:

   ```bash
   poetry add requests
   ```

   * Remove dependencies:

   ```bash
   poetry remove requests
   ```

   * Install all dependencies:

   ```bash
   poetry install
   ```

---

### 🔹 Quick Start

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Create a new project
poetry new my-project

# Navigate into project
cd my-project

# Install dependencies from pyproject.toml
poetry install

# Activate the project’s virtual environment
poetry shell
```

---

✅ **Summary:**
Poetry provides a **modern, reliable, and reproducible** way to manage Python project dependencies, virtual environments, and packaging for distribution.

---