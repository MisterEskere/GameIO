from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt, QTimer

from fitgirl import fitgirl_search, fitgirl_get_downloadlink
from downloader import download_game, download_status

def update_search_results(query, list_widget):
    results = fitgirl_search(query)
    list_widget.clear()  # Clear existing items
    for result in results:
        item = QListWidgetItem(result.name)
        item.setData(Qt.ItemDataRole.UserRole, result)  # Store the entire game object
        list_widget.addItem(item)

def update_download_status(download_status_list):
    download_status_list.clear()  # Clear existing items
    for status in download_status:
        download_status_list.addItem(status)

def create_window():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('GameIO')
    
    search_bar = QLineEdit(window)
    search_bar.move(100, 100)
    search_bar.resize(280, 40)
    search_bar.setPlaceholderText('Search for games...')

    search_button = QPushButton(window)
    search_button.move(400, 100)
    search_button.resize(100, 40)
    search_button.setText('Search')
    search_results = QListWidget(window)
    search_results.move(100, 150)
    search_results.resize(400, 200)
    search_button.clicked.connect(lambda: update_search_results(search_bar.text(), search_results))

    download_button = QPushButton(window)
    download_button.move(100, 360)
    download_button.resize(400, 40)
    download_button.setText('Download')
    download_button.clicked.connect(lambda: fitgirl_get_downloadlink(search_results.currentItem().data(Qt.ItemDataRole.UserRole)))

    download_status_list = QListWidget(window)
    download_status_list.move(100, 410)
    download_status_list.resize(400, 200)
    update_download_status(download_status_list)  # Initial update

    # Set up a timer to refresh the download status list every second
    timer = QTimer(window)
    timer.timeout.connect(lambda: update_download_status(download_status_list))
    timer.start(1000)  # Update every 1000 milliseconds (1 second)

    window.show()
    app.exec()

create_window()