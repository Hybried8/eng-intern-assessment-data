import sqlite3

def run_sql_script(sql_file):
    # Connect to SQLite database
    conn = sqlite3.connect('mod_shopify_data.db')
    cursor = conn.cursor()

    try:
        # Read SQL query from file
        with open(sql_file, 'r') as file:
            query = file.read()

        # Execute SQL query
        cursor.execute(query)

        # Fetch and print query results
        for row in cursor.fetchall():
            print(row)

    except sqlite3.Error as e:
        print("Error executing SQL query:", e)

    finally:
        # Close database connection
        conn.close()

if __name__ == "__main__":
    # Specify the paths to your SQL files
    sql_files = ['task1.sql', 'task2.sql', 'task3.sql']

    # Run the SQL scripts
    for sql_file in sql_files:
        print(f"Executing SQL script: {sql_file}")
        run_sql_script(sql_file)
        print("\n")
