from PySide6.QtWidgets import QPushButton, QWidget


class Button(QPushButton):
    def __init__(self,  text: str) -> None:
        super().__init__()
        self.setMinimumSize(75, 75)
        self.setText(text)
        self.setStyleSheet(f'font-size:{10}px')
