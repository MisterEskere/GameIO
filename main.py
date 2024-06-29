from fitgirl import fitgirl_search, fitgirl_get_downloadlink

# Specify the DNS server and the domain
game = input("Enter the game you want to search for: ")

games = fitgirl_search(game)

game = games[0]
link = fitgirl_get_downloadlink(game)

print(link)