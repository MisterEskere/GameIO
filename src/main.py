from fitgirl import fitgirl_search, fitgirl_get_downloadlink
from downloader import download_game_threaded
from database import create_db

# Create the database
create_db()

while True:
    game = input("Enter the game you want to search for: ")

    games = fitgirl_search(game)

    if len(games) == 0:
        print("No games found.")
        exit()

    game = games[0]
    link = fitgirl_get_downloadlink(game)
    download_game_threaded(link)

    game = games[1]
    link = fitgirl_get_downloadlink(game)
    download_game_threaded(link)
    
    game = games[2]
    link = fitgirl_get_downloadlink(game)
    download_game_threaded(link)
