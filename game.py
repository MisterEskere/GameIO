# class games with name and link attributes

class Game:
    def __init__(self, id, name, link, Genre, Companies, Lenguages, GameSize, DownloadSize):
        self.id = id
        self.name = name
        self.link = link
        self.Genres = Genre
        self.Companies = Companies
        self.Lenguages = Lenguages
        self.GameSize = GameSize
        self.DownloadSize = DownloadSize
        
    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nLink: {self.link}\nGenres: {self.Genres}\nCompanies: {self.Companies}\nLenguages: {self.Lenguages}\nGame Size: {self.GameSize}\nDownload Size: {self.DownloadSize}"