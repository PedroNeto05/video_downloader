from PySide6.QtWidgets import QApplication, QComboBox, QCheckBox
from main_window import MainWindow
from button import Button
from url_input import UrlInput
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    # Input de url para buscar o video
    urlInput = UrlInput()
    buttonSearch = Button('Search')
    mainWindow.addWidgetsInUrlInputLayout(urlInput, buttonSearch)

    comboBox = QComboBox()
    checkBox = QCheckBox()
    buttonAddVideo = Button('Add')

    mainWindow.addWidgetsInOptionsLayout(comboBox, checkBox)
    mainWindow.addWidgetsInVideoConfigLayout(buttonAddVideo)

    mainWindow.show()
    app.exec()
