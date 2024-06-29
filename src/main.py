import libtorrent as lt
from fitgirl import fitgirl_search, fitgirl_get_downloadlink
import dotenv
import time

# Load the environment variables
dotenv.load_dotenv()

# Specify the DNS server and the domain
game = input("Enter the game you want to search for: ")

games = fitgirl_search(game)

game = games[0]
link = fitgirl_get_downloadlink(game)

# get the download path from the environment variables
env = dotenv.dotenv_values()
download_path = env.get("DOWNLOAD_PATH")

# sets the session settings, dont edit this
ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})
params = lt.parse_magnet_uri(link)

# set the save path
params.save_path = download_path # TODO this will be changed in the .env file from the rust side

# set the storage mode to storage_mode_allocate
params.storage_mode = lt.storage_mode_t(2) # TODO in the future this will be an option in the .env file from the rust side

# Add the torrent to the session
handle = ses.add_torrent(params)

# Wait for the torrent to be ready for download
while not handle.torrent_file():
    time.sleep(1)

# 
while handle.status().state != lt.torrent_status.seeding:
    s = handle.status()
    time.sleep(1)
