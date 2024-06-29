import libtorrent as lt
import dotenv
import time

# get the download path from the environment variables
env = dotenv.dotenv_values()
download_path = env.get("DOWNLOAD_PATH")

ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

def download_game(link, download_path, storage_mode=2):
    """
    Downloads a game using the magnet link.
    
    Args:
        link (str): The magnet link of the game.
        download_path (str): The path where the game will be downloaded.
        storage_mode (int): The storage mode of the game.
        
    Returns:
        None
    """

    params = lt.parse_magnet_uri(link)
    params.save_path = download_path
    params.storage_mode = lt.storage_mode_t(storage_mode)
    
    handle = ses.add_torrent(params)
    while not handle.torrent_file():
        time.sleep(1)
    
    while handle.status().state != lt.torrent_status.seeding:
        s = handle.status()
        time.sleep(1)
    
    return True
