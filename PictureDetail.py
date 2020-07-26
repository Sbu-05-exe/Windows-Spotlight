import PyQt5, sys
from PyQt5.QtWidgets import QWidget, QLabel, QListWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtGui import QPixmap

class PictureDisplay(QWidget):
	def __init__(self, activeImage = None, images = None, path= None):
		super().__init__()
		self.activeImage, self.images, self.path = activeImage, images, path

		self.picture = None
		setting_layout, self.btnBackward, self.btnForward = self.create_layout()
		self.setLayout(setting_layout)
		self.setPicture()
		self.show()

	def create_layout(self):
		self.picture = QLabel()

		hbox = QHBoxLayout()
		btnForward = QPushButton(self)
		btnBackward = QPushButton(self)

		# Making widgets reponsive

		btnForward.setSizePolicy(QP.Preferred, QP.Expanding)
		btnBackward.setSizePolicy(QP.Preferred, QP.Expanding)
		self.picture.setSizePolicy(QP.Expanding, QP.Expanding)

		btnForward.setText('-->')
		btnBackward.setText('<--')

		btnForward.clicked.connect(lambda: self.nextpic(1))
		btnBackward.clicked.connect(lambda :self.nextpic(-1))

		hbox.addWidget(btnBackward)
		hbox.addWidget(self.picture)
		hbox.addWidget(btnForward)

		return hbox, btnBackward, btnForward

	def setPicture(self):
		if self.activeImage:
			# set the picture on the screen

			src = self.path + '/' + self.activeImage

			pixmap = QPixmap(self.path + '/'+ self.activeImage)
			height, width = pixmap.height(), pixmap.width()
			print('Dimensions', height,'x',width)

			pixmap = pixmap.scaled(500, 300)
			self.picture.setPixmap(pixmap)

			# Button control
			print(self.activeImage in self.images)

			if self.activeImage in self.images:
				index = (self.images.index(self.activeImage))

			else:
				index = 0

			if index == 0:
				self.btnBackward.setEnabled(False)
				self.btnForward.setEnabled(True)

			elif index == len(self.images)-1:
				self.btnForward.setEnabled(False)
				self.btnBackward.setEnabled(True)

			else:
				self.btnForward.setEnabled(True)
				self.btnBackward.setEnabled(True)



		else:
			self.btnForward.setEnabled(False)
			self.btnBackward.setEnabled(False)

	def nextpic(self, forward=1):
		index = (self.images.index(self.activeImage))
		index = index + forward
		self.activeImage = self.images[index]
		self.setPicture()

	def setImages(self,images):
		self.Images = images

	def setActiveImage(self, image):
		self.activeImage = image

	def setPath(self, path):
		self.path = path


def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Settings')

	PicDisplay = PictureDisplay()
	PicDisplay.show()
	sys.exit(App.exec_())

if __name__ == "__main__":
	main()