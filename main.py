#Repository link: https://github.com/Mikey-Z45/Team_Project_205.git
#webscraper.py
#11/20/2017
#Michae Divis, Jessica Ubaldo
#Description: GUI for the program, opens a window which lets a user input an address and press Submit.
#then displays images after face detection in a scrollable window.
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QVBoxLayout, QComboBox, QGroupBox, QScrollArea)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image

class Window(QWidget):


	def __init__(self):
			super().__init__()
			self.initUI()

	def initUI(self):
			self.label = QLabel("Enter URL here: ", self)

			self.textbox = QLineEdit()
			self.button = QPushButton('Submit URL', self)

			# connect button to function on_click
			self.button.clicked.connect(self.on_click)

			# create vertical box layout for GUI
			layout = QVBoxLayout()

			# global layout that'll take in the new pictures
			global layout2
			layout2 = QVBoxLayout()

			# group box
			global groupBox
			groupBox = QGroupBox()

			# scroller area
			global scroller
			scroller = QScrollArea()

			# add widgets for label and line edit
			layout.addWidget(self.label)
			layout.addWidget(self.textbox)
			layout.addWidget(self.button)



			# the images are added to the original layout/GUI
			layout.addWidget(scroller)

			# set the layout
			self.setLayout(layout)
			self.setWindowTitle("New Window Here")
			self.show()

	def on_click(self):
		textboxValue = self.textbox.text()

		inputURL = textboxValue

		with open("currentURL.txt", "w") as file:
			file.write(inputURL)

		# import the file that'll read faces from images
		import webscraper
		import face_reader

		# for-loop to go through every image and display them
		x = 1
		for x in range(16):
			self.img = QPixmap('faceimages/' + str(x) + '.jpg')
			self.picLabel = QLabel()
			self.picLabel.setPixmap(self.img)
			layout2.addWidget(self.picLabel)
			x+=1
			print(x)

		groupBox.setLayout(layout2)
		scroller.setWidget(groupBox)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())
