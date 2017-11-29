# Intro
# textBox.py
# Michael Divis
# 9/18/17
# Description: Creates a nested layout that contains buttons and text.
# Python 3.6.0

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = '205 Project: URL input box'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create a message box
        self.QMessageBox.setText("Enter the URL to find faces.")
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
 
        # Create a button in the window to submit the url
        self.button = QPushButton('Submit URL', self)
        self.button.move(20,80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

# this is where we can pass the input web address from the user to our variable to search with
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
