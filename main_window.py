from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Downloader')

        self.cw = QWidget()
        self.rootVLayout = QHBoxLayout()
        self.cw.setLayout(self.rootVLayout)
        self.setCentralWidget(self.cw)

        self._downloadQueueLayout = QVBoxLayout()
        self._addVideoInQueueLayout = QVBoxLayout()

        self.urlInputLayout = QHBoxLayout()
        self.videoConfigLayout = QVBoxLayout()

        self.optionsLayout = QHBoxLayout()

        self._addLayoutsInRootLayout()
        self._addLayoutsInDownloadQueueLayout()
        self._addLayoutsInAddVideoInQueueLayout()
        self._addLayoutsInVideoConfigLayout()

    def _addLayoutsInRootLayout(self):
        self.rootVLayout.addLayout(self._downloadQueueLayout)
        self.rootVLayout.addLayout(self._addVideoInQueueLayout)

    def _addLayoutsInDownloadQueueLayout(self):
        pass

    def _addLayoutsInAddVideoInQueueLayout(self):
        self._downloadQueueLayout.addLayout(self.urlInputLayout)
        self._downloadQueueLayout.addLayout(self.videoConfigLayout)

    def _addLayoutsInVideoConfigLayout(self):
        self.videoConfigLayout.addLayout(self.optionsLayout)

    def addWidgetsInUrlInputLayout(self, *widgets: QWidget):
        for widget in widgets:
            self.urlInputLayout.addWidget(widget)

    def addWidgetsInOptionsLayout(self, *widgets: QWidget):
        for widget in widgets:
            self.optionsLayout.addWidget(widget)

    def addWidgetsInVideoConfigLayout(self, *widgets: QWidget):
        for widget in widgets:
            self.videoConfigLayout.addWidget(widget)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
