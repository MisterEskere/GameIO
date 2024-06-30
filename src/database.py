import sqlite3

def create_db():
    # Define the paths
    sql_file_path = 'create_tables.sql'
    db_path = 'database.sqlite'

    # Open and read the .sql file
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.executescript(sql_script)
    except sqlite3.OperationalError as e:
        pass

    conn.commit()
    cursor.close()
    conn.close()
