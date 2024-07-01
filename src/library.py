from database import connect_db

# --------------------------------------
class game_in_library:
    """
    A class to represent the games table in the database using SQLAlchemy.
    This will be used to track the user's library of games.
    """
    def __init__(self, game_id, game_name, download_progress, download_location, download_status, download_info, install_location, executable_location):
        self.game_id = game_id
        self.game_name = game_name
        self.download_progress = download_progress
        self.download_location = download_location
        self.download_status = download_status
        self.download_info = download_info
        self.install_location = install_location
        self.executable_location = executable_location

    def __repr__(self):
        return f"Games(game_id={self.game_id}, game_name={self.game_name}, download_progress={self.download_progress}, download_location={self.download_location}, download_status={self.download_status}, download_info={self.download_info}, install_location={self.install_location}, executable_location={self.executable_location})"

    def __str__(self):
        return f"Game: {self.game_name} | Download Progress: {self.download_progress} | Download Location: {self.download_location} | Download Status: {self.download_status} | Download Info: {self.download_info} | Install Location: {self.install_location} | Executable Location: {self.executable_location}"

# --------------------------------------
def add_game(game_id, game_name, download_progress, download_location, download_status, download_info, install_location, executable_location):
    """
    Adds a game to the database.
    Used when a players installs a new game.
    """
    conn, cursor = connect_db()

    cursor.execute("INSERT INTO games (game_id, game_name, download_progress, download_location, download_status, download_info, install_location, executable_location) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (game_id, game_name, download_progress, download_location, download_status, download_info, install_location, executable_location))

    conn.commit()
    cursor.close()
    conn.close()

# --------------------------------------
def get_game(game_id):
    """
    Gets a game from the database.
    Used when a player wants to see the details of a game in their library.
    """
    conn, cursor = connect_db()

    cursor.execute("SELECT * FROM games WHERE game_id = ?", (game_id,))
    game = cursor.fetchone()

    cursor.close()
    conn.close()

    return game

# --------------------------------------
def get_all_games():
    """
    Gets all the games from the database.
    Used when a player wants to see their library of games.
    """
    conn, cursor = connect_db()

    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()

    cursor.close()
    conn.close()

    return games

# --------------------------------------
def update_game(game_id, download_progress, download_location, download_status, download_info, install_location, executable_location):
    """
    Updates a game in the database.
    Used when a player installs a game or when a game's download status changes.
    """
    conn, cursor = connect_db()

    cursor.execute("UPDATE games SET download_progress = ?, download_location = ?, download_status = ?, download_info = ?, install_location = ?, executable_location = ? WHERE game_id = ?", (download_progress, download_location, download_status, download_info, install_location, executable_location, game_id))

    conn.commit()
    cursor.close()
    conn.close()

# --------------------------------------
def delete_game(game_id):
    """
    Deletes a game from the database.
    Used when a player uninstalls a game.
    """
    conn, cursor = connect_db()

    cursor.execute("DELETE FROM games WHERE game_id = ?", (game_id,))

    conn.commit()
    cursor.close()
    conn.close()
