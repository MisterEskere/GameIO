import requests
import dns.resolver
from bs4 import BeautifulSoup
from src.game import Game

dns_server = '8.8.8.8'
domain = 'fitgirl-repacks.site'
resolver = dns.resolver.Resolver()
resolver.nameservers = [dns_server]
ip_address = resolver.resolve(domain, 'A')[0].to_text()
headers = {'Host': domain}

def fitgirl_search(game : str):
    """
    Search for a game on the FitGirl Repacks website and return the results.
    :param game: The game to search for.
    :return: A list of Game objects.
    """

    # Create the URL with the IP address and set the Host header to the original domain
    url = f"https://{ip_address}/?s={game}"

    # Make the request
    try:
        response = requests.get(url, headers=headers, verify=True)
    except:
        response = requests.get(url, headers=headers, verify=False)

    # print all the <article> tags
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    games = []
    for article in articles:
        
        # id of the game
        id = article['id']
        id = id.replace('post-', '')

        # data about the game
        entry_summary = article.find('div', class_='entry-summary')
        entry_summary_a = entry_summary.find('a')
        entry_summary_p = entry_summary.find('p').text
    
        # link of the game
        link = entry_summary_a['href']
        link = link.replace(domain, ip_address)
        
        # name of the game
        name = entry_summary_a.find('span', class_='screen-reader-text').text

        # genre of the game
        # look for "Genres/Tags:" text in the entry_summary_p
        # if founnd get the position of the text
        if "Genres/Tags:" in entry_summary_p:
            genres_start = entry_summary_p.find("Genres/Tags:")

        if "Companies:" in entry_summary_p:
            companies_start = entry_summary_p.find("Companies:")
        if "Company:" in entry_summary_p:
            companies_start = entry_summary_p.find("Company:")

        if "Language:" in entry_summary_p:
            lenguages_start = entry_summary_p.find("Language:")
        if "Languages:" in entry_summary_p:
            lenguages_start = entry_summary_p.find("Languages:")

        if "Original Size:" in entry_summary_p:
            game_size_start = entry_summary_p.find("Original Size:")
        if "Repack Size:" in entry_summary_p:
            download_size_start = entry_summary_p.find("Repack Size:")
        if "Download Mirrors" in entry_summary_p:
            download_size_end = entry_summary_p.find("Download Mirrors")

        # get the genres
        genres = entry_summary_p[genres_start:companies_start]
        genres = genres.replace("Genres/Tags:", "")
        genres = genres.split(',')
        genres = [genre.strip() for genre in genres]

        # get the companies
        companies = entry_summary_p[companies_start:lenguages_start]
        companies = companies.replace("Companies:", "")
        companies = companies.replace("Company:", "")
        companies = companies.split(',')
        companies = [company.strip() for company in companies]
        
        # get the lenguages
        lenguages = entry_summary_p[lenguages_start:game_size_start]
        lenguages = lenguages.replace("Languages:", "")
        lenguages = lenguages.replace("Language:", "")
        lenguages = lenguages.split('/')
        lenguages = [lenguage.strip() for lenguage in lenguages]
        
        # get the game size
        game_size = entry_summary_p[game_size_start:download_size_start]
        game_size = game_size.replace("Original Size:", "")
        game_size = game_size.strip()
        
        # get the download size
        download_size = entry_summary_p[download_size_start:download_size_end]
        download_size = download_size.replace("Repack Size:", "")
        download_size = download_size.strip()

        # create a Game object and append it to the games list
        game = Game(id, name, link, genres, companies, lenguages, game_size, download_size)
        games.append(game)
    
    return games

def fitgirl_get_downloadlink(game : Game):
    """
    Get the download link for a game from the FitGirl Repacks website.
    :param game: The Game object to get the download link for.
    :return: The download link.
    """

    # Make the request to the game's page
    # Create the URL with the IP address and set the Host header to the original domain
    url = game.link

    # Make the request
    try:
        response = requests.get(url, headers=headers, verify=True)
    except:
        response = requests.get(url, headers=headers, verify=False)

    # game download link extraction
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    entry_content = article.find('div', class_='entry-content')
    ul_1 = entry_content.find_all('ul')[1]
    li_1 = ul_1.find_all('li')
    a_1 = li_1[0].find_all('a')[1]
    link = a_1['href']

    return link 
