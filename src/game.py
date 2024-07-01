class Game:
    """
    A class to represent a game with various properties.
    """
    def __init__(self, id: str, name: str, link: str, genres: list, companies: list, languages: list, game_size: str, download_size: str):
        self.id = id
        self.name = name
        self.link = link
        self.genres = genres
        self.companies = companies
        self.languages = languages
        self.game_size = game_size
        self.download_size = download_size
        self.magnet_link = ""

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nLink: {self.link}\nGenres: {self.genres}\nCompanies: {self.companies}\nLanguages: {self.languages}\nGame Size: {self.game_size}\nDownload Size: {self.download_size}"

    def update_magnet_link(self, magnet_link: str):
        self.magnet_link = magnet_link
