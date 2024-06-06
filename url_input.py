from PySide6.QtWidgets import QLineEdit
from variables import FONT_SIZE_LARGE, MIN_INPUT_URL_WIDTH, DEFAULT_MARGIN
from PySide6.QtCore import Qt


class UrlInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size:{FONT_SIZE_LARGE}px")
        self.setMinimumHeight(FONT_SIZE_LARGE*2)
        self.setMinimumWidth(MIN_INPUT_URL_WIDTH)
        self.setTextMargins(*[DEFAULT_MARGIN for _ in range(4)])
        pass
