import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
import os

class RegistrationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Account Registration"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 300, 200)

        # Create layout
        layout = QVBoxLayout()

        # Username
        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit(self)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        # Email
        self.email_label = QLabel("Email:", self)
        self.email_input = QLineEdit(self)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Password
        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Register Button
        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.register_account)
        layout.addWidget(self.register_button)

        # Set layout
        self.setLayout(layout)

    def register_account(self):
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        # Check for empty fields
        if not username or not email or not password:
            self.show_message("Error", "Please fill in all fields", QMessageBox.Critical)
            return

        # Save to .csv file
        try:
            with open('accounts.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, email, password])
            self.show_message("Success", "Registration successful!", QMessageBox.Information)
        except Exception as e:
            self.show_message("Error", f"An error occurred: {e}", QMessageBox.Critical)

    def show_message(self, title, message, icon_type):
        msg_box = QMessageBox(self)
        msg_box.setIcon(icon_type)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationApp()
    ex.show()
    sys.exit(app.exec_())
