from fitgirl import fitgirl_search, fitgirl_get_downloadlink
from downloader import download_game
import threading
from database import create_db

# Create the database
create_db()

def download_game_threaded(link):
    thread = threading.Thread(target=download_game, args=(link,))
    thread.start()

while True:
    game = input("Enter the game you want to search for: ")

    games = fitgirl_search(game)

    if len(games) == 0:
        print("No games found.")
        exit()

    game = games[0]
    link = fitgirl_get_downloadlink(game)

    # download the game
    download_game_threaded(link)
