import sqlite3

# --------------------------------------
def create_db():
    """
    Creates the database and the tables.
    """
    
    # Define the paths
    sql_file_path = 'create_library.sql'
    db_path = 'library.sqlite'

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

# --------------------------------------
def connect_db():
    """
    Connects to the database and returns the connection and cursor.
    """

    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    return conn, cursor
