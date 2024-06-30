import requests
import dns.resolver
from bs4 import BeautifulSoup
from game import Game
import uuid
import os

# set data for web scraping
dns_server = '8.8.8.8'
domain = 'fitgirl-repacks.site'
resolver = dns.resolver.Resolver()
resolver.nameservers = [dns_server]
ip_address = resolver.resolve(domain, 'A')[0].to_text()
headers = {'Host': domain}

#------------------------------------------------------------
def fitgirl_search(game : str):
    """
    Search for a game on the FitGirl Repacks website and return the results.
    :param game: The game to search for.
    :return: A list of Game objects.
    """

    # connect to the website with the search query
    url = f"https://{ip_address}/?s={game}"

    # Make the request to get the page
    try:
        response = requests.get(url, headers=headers, verify=True)
    except:
        response = requests.get(url, headers=headers, verify=False)

    # Web scraping
        soup = BeautifulSoup(response.text, 'html.parser')
        
        try:
            articles = soup.find_all('article')
        except:
            pages_bug("missing_articles", response.text)
            return False

        games = []
        for i, article in enumerate(articles):

            # id of the game
            try:
                id = article['id']
            except:
                pages_bug("missing_id", article)
                continue

            # check if the article is a game
            try:
                category = article.find('span', class_='cat-links').text
                if category != 'Lossless Repack':
                    raise ValueError("Not a game")
            except:
                pages_bug("not_a_game", article)
                continue

            try:
                entry_summary = article.find('div', class_='entry-summary')
                if entry_summary is None:
                    raise ValueError("No entry_summary")
            except:
                pages_bug("missing_entry_summary", article)
                continue

            # link and name of the game
            try:
                entry_summary_a = entry_summary.find('a')
                if entry_summary_a is None:
                    raise ValueError("No entry_summary_a")
            except:
                pages_bug("missing_entry_summary_a", entry_summary)
                continue

            # link of the game
            try:
                link = entry_summary_a['href']
                link = link.replace(domain, ip_address)
            except:
                pages_bug("missing_link", entry_summary_a)
                continue

            # name of the game
            try:
                name = entry_summary_a.find('span', class_='screen-reader-text').text
            except:
                pages_bug("missing_name", entry_summary_a)
                continue

            # information about the game
            try:
                entry_summary_p = entry_summary.find('p').text
                if entry_summary_p is None:
                    raise ValueError("No entry_summary_p")
            except:
                pages_bug("missing_entry_summary_p", entry_summary)
                continue

            try:
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
            except:
                pages_bug("missing_information", entry_summary_p)
                continue

            # create a Game object and append it to the games list
            game = Game(id, name, link, genres, companies, lenguages, game_size, download_size)
            games.append(game)
    
    return games

# ------------------------------------------------------------
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
    try:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            article = soup.find('article')
        except:
            pages_bug("missing_article", response.text)
            return False

        try:
            entry_content = article.find('div', class_='entry-content')
        except:
            pages_bug("missing_entry_content", article)
            return False
    
        try:
            ul_1 = entry_content.find_all('ul')[1]
        except:
            pages_bug("missing_ul_1", entry_content)
            return False
    
        try:
            li_1 = ul_1.find_all('li')
        except:
            pages_bug("missing_li_1", ul_1)
            return False
    
        try:
            a_1 = li_1[0].find_all('a')[1]
        except:
            pages_bug("missing_a_1", li_1)
            return False    
        
        try:
            link = a_1['href']
        except:
            pages_bug("missing_link", a_1)
            return False

    except Exception as e:
        pages_bug(e, response.text)
        return False

    return link

# ------------------------------------------------------------
def pages_bug(error, page):
    """
    This function is used to save pages that caused errors with the name of the error"
    """

    random_id = uuid.uuid4()
    directory = 'bugs_htmls'
    name = f'{directory}/error_{error}_{random_id}.html'

    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(name, 'w') as file:
        file.write(str(page))

    return name