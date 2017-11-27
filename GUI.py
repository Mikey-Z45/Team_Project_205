# Intro
# LAB_9.py
# Michael Divis
# 9/18/17
# Description: Creates a nested layout that contains buttons and text.
# Python 3.6.0

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox,
                                QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtCore import pyqtSlot

class MyWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.create_label()
        self.createButtonBox()
        self.createBorderBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.border_box)
        self.setLayout(mainLayout)
        self.setWindowTitle("Webscraper Project")
        self.show()

     
        
    def create_label(self):
        my_string = "<h1>CST 205</h1><p>This is part of the final project.</p>"
        self.group_box = QGroupBox("Message Box")
        v_layout = QVBoxLayout()
        my_label = QLabel(self)
        my_label.setText(my_string)
        v_layout.addWidget(my_label)
        self.group_box.setLayout(v_layout)

    def createButtonBox(self):
        self.horizontalGroupBox = QGroupBox("Buttons")
        v_layout = QVBoxLayout()
        for i in range(5):
            my_button = QPushButton(f"Button {i+1}")
            my_button.clicked.connect(self.on_click)
            v_layout.addWidget(my_button)
        self.horizontalGroupBox.setLayout(v_layout)


    def createBorderBox(self):
        self.border_box = QGroupBox("Container layout")
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.group_box)
        h_layout.addWidget(self.horizontalGroupBox)
        self.border_box.setLayout(h_layout)

    #  pyqtSlot() function decorator to create a Qt slot
    @pyqtSlot()
    def on_click(self):
        button = self.sender()
        print(button.text())

my_app = QApplication(sys.argv)
a_window = MyWindow()
sys.exit(my_app.exec_())
'''
SAMPLE OUTPUT:



 
'''
