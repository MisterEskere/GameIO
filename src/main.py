import libtorrent as lt
from fitgirl import fitgirl_search, fitgirl_get_downloadlink
import dotenv
import time
from downloader import download_game

# Load the environment variables
dotenv.load_dotenv()

# Specify the DNS server and the domain
game = input("Enter the game you want to search for: ")

games = fitgirl_search(game)
print("Games found:")
print(len(games))

for game in games:
    print(game)

input("Press Enter to continue...")

if len(games) == 0:
    print("No games found.")
    exit()

game = games[0]
link = fitgirl_get_downloadlink(game)

# download the game
download_game(link)