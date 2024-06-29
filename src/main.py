import libtorrent as lt
from src.fitgirl import fitgirl_search, fitgirl_get_downloadlink

# Specify the DNS server and the domain
game = input("Enter the game you want to search for: ")

games = fitgirl_search(game)

game = games[0]
link = fitgirl_get_downloadlink(game)

# download the magnet link with libtorrent
ses = lt.session()
ses.listen_on(6881, 6891)

