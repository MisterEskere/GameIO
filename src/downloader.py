import libtorrent as lt
import dotenv
import time

# get the download path from the environment variables
env = dotenv.dotenv_values()
download_path = env.get("DOWNLOAD_PATH")
storage_mode = env.get("STORAGE_MODE")

ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

# sets no limit to the session for maximum download speed
ses_settings = {
    'active_downloads': -1,
    'active_seeds': -1,
    'active_limit': -1,
    'auto_manage_startup': 200,
    'auto_manage_interval': 30,
    'connections_limit': -1,
    'download_rate_limit': -1,
    'upload_rate_limit': -1
}

def download_game(link):
    """
    Downloads a game using the magnet link.

    Args:
        link (str): The magnet link of the game.

    Returns:
        None
    """

    try:
        params = lt.parse_magnet_uri(link)
        params.save_path = download_path
        params.storage_mode = lt.storage_mode_t(storage_mode)
        
        handle = ses.add_torrent(params)
        while not handle.torrent_file():
            print("Downloading metadata...")
            time.sleep(1)
        
        while handle.status().state != lt.torrent_status.seeding:
            s = handle.status()
    
            # retrive all the information about the torrent
            donload_speed = s.download_rate / 1000000
            progress = s.progress * 100

            print(f"Download Speed: {donload_speed:.2f} MB/s | Progress: {progress:.2f}%")
            
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    print("Download completed.")
    return True
