"""
Pickle Basics in Python
-----------------------

Pickle is a Python module used for **serialization** and **deserialization** of Python objects 
using a binary protocol. 

- **Serialization (pickling):** Converts a Python object into a byte stream (for saving or transmission).
- **Deserialization (unpickling):** Converts that byte stream back into the original Python object.

When to Use:
    - Saving/loading Python objects (lists, dicts, custom classes) for your own programs
    - Storing model states or intermediate data within the same Python environment
    - Quick local caching for prototyping

When NOT to Use:
    - Never load untrusted `.pkl` files (security risk)
    - Avoid for long-term storage or cross-language communication
    - Use JSON/CSV/Parquet for data meant to be shared or versioned

Pickle is also commonly used in:
    - Saving NumPy arrays
    - Saving Pandas DataFrames (faster than CSV for large datasets)
    - Saving trained machine learning models for reuse
"""

import pickle

# Example 1: Simple Dictionary
students = {
    'student 1': {'Name': "Alice", 'Roll': 10, 'Grade': 4},
    'student 2': {'Name': "Bob", 'Roll': 11, 'Grade': 4},
    'student 3': {'Name': "Elena", 'Roll': 12, 'Grade': 5}
}

# Check object type
print(type(students))  # <class 'dict'>


# Example 2: Serialize (Save) a List
student_names = ['Alice', 'Bob', 'Elena', 'Jane']

with open('student_file.pkl', 'wb') as f:
    pickle.dump(student_names, f)  # Serialize object to file

print(" student_file.pkl saved successfully.")


# Example 3: Deserialize (Load) the List
with open('student_file.pkl', 'rb') as f:
    student_names_loaded = pickle.load(f)  # Load object from file

print("Loaded student names:", student_names_loaded)


# ------------------------------------------------------------------------
# Example 4: Using Pickle with NumPy Arrays and Pandas DataFrames
# ------------------------------------------------------------------------

"""
Pickle is often used to store NumPy arrays and Pandas DataFrames.
While CSV is human-readable, Pickle is much faster for large data
because it stores the entire object structure directly.
"""

# Uncomment these examples if NumPy/Pandas are installed:
"""
import numpy as np
import pandas as pd

# Save a NumPy array
array = np.array([1, 2, 3, 4, 5])
with open('array.pkl', 'wb') as f:
    pickle.dump(array, f)

# Load the array
with open('array.pkl', 'rb') as f:
    loaded_array = pickle.load(f)
print("Loaded NumPy array:", loaded_array)

# Save a Pandas DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Score': [90, 85]})
df.to_pickle('dataframe.pkl')

# Load the DataFrame
loaded_df = pd.read_pickle('dataframe.pkl')
print("Loaded DataFrame:")
print(loaded_df)
"""

# ------------------------------------------------------------------------
# Example 5: Serializing Machine Learning Models
# ------------------------------------------------------------------------

"""
Pickle is also used for saving trained ML models so they can be reloaded
without retraining every time.

Example:
    pickle.dump(model, open('model.pkl', 'wb'))
    model = pickle.load(open('model.pkl', 'rb'))
"""

print("\n Tip: Use Joblib for large ML models — it’s optimized for NumPy arrays.")
