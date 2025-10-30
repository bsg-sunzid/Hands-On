import psycopg2
import pandas as pd

# Connection parameters
host = "localhost"
port = 5432
database = "my_database"
user = "postgres"
password = "sunzid123"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute a query
    query = "SELECT * FROM employees;"
    cur.execute(query)

    # Fetch all results
    rows = cur.fetchall()

    # Get column names
    colnames = [desc[0] for desc in cur.description]

    # Convert to Pandas DataFrame
    df = pd.DataFrame(rows, columns=colnames)

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Show the DataFrame
    print(df.head())

except Exception as e:
    print("Error connecting to PostgreSQL:", e)
