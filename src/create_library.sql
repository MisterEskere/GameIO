CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id TEXT,
    game_name TEXT,
    download_progress INTEGER,
    download_location TEXT,
    download_status TEXT CHECK(download_status IN ('PAUSED', 'RUNNING', 'COMPLETED', 'FAILED')),
    download_info TEXT,
    install_location TEXT,
    executable_location TEXT
);