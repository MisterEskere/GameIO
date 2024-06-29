from fitgirl import fitgirl_search, fitgirl_game_info

# Specify the DNS server and the domain
game = input("Enter the game you want to search for: ")

games = fitgirl_search(game)


for game in games:
    print("----------------")
    print(game)
    print("----------------")

#game = games[0]
#game_details = fitgirl_game_info(game)
#print(game_details)