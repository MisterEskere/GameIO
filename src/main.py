from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QListWidget

from fitgirl import fitgirl_search

def create_window():
    app = QApplication([])
    window = QWidget()

    # Set the window title
    window.setWindowTitle('GameIO')
    
    # add a search bar in the middle of the window
    search_bar = QLineEdit(window)
    search_bar.move(100, 100)
    search_bar.resize(280, 40)
    search_bar.setPlaceholderText('Search for games...')

    # add a search button that will call the fitgirl_search function and store the results in a list
    search_button = QPushButton(window)
    search_button.move(400, 100)
    search_button.resize(100, 40)
    search_button.setText('Search')
    search_button.clicked.connect(lambda: fitgirl_search(search_bar.text()))

    # show the results of the search in a list
    search_results = QListWidget(window)
    search_results.move(100, 150)
    search_results.resize(400, 200)
    

    window.show()
    app.exec()
 
create_window()
