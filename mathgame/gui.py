from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton

from PySide6.QtCore import Qt

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Solve the Equation")
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)
        label = QLabel("Solve the Equation")
        question = QLabel("Here is question")
        button = QPushButton("Enter")
        button.clicked.connect()
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(question)
        layout.addWidget(line_edit)
        layout.addWidget(button)
        
       

app = QApplication()

window = Main_Window()
window.show()

app.exec()

