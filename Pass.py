import random
import string
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

def generate_password(length=8):
    # Generate a random string of lowercase letters, uppercase letters, and digits
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

class PasswordWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label to display the password
        self.password_label = QLabel()
        self.password_label.setText("Click the button to generate a password")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_label.setStyleSheet("font-size: 18px;")

        # Create a button to generate a new password
        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_button.setStyleSheet("font-size: 18px;")

        # Create a button to copy the password to the clipboard
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_password)
        self.copy_button.setStyleSheet("font-size: 18px;")

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.copy_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def generate_password(self):
        # Generate a password and display it in the label
        password = generate_password()
        self.password_label.setText(f"This is your password: {password}")

    def copy_password(self):
        # Get the password from the label and copy it to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_label.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordWindow()
    window.show()
    sys.exit(app.exec_())