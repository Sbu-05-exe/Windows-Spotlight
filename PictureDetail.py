import App
import PyQt5, sys
from PyQt5.QtWidgets import QWidget, QLabel, QListWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtGui import QPixmap

class PictureDisplay(QWidget):
	def __init__(self):
		super().__init__()
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
		btnBackward.clicked.connect(lambda :self.nextpic(-1) )

		print(dir(btnBackward))

		hbox.addWidget(btnBackward)
		hbox.addWidget(self.picture)
		hbox.addWidget(btnForward)

		return hbox, btnBackward, btnForward

	def setFn(self):
		self.setPicture

	def setPicture(self):
		pixmap = QPixmap(App.dirs['cd'] + App.activeImage)

		index = (App.images.index(App.activeImage))

		if index == 0:
			self.btnBackward.setEnabled(False)
			self.btnForward.setEnabled(True)

		elif index == (len(App.images) -1):
			self.btnForward.setEnabled(False)
			self.btnBackward.setEnabled(True)

		else:
			self.btnForward.setEnabled(True)
			self.btnBackward.setEnabled(True)

		print('height:', pixmap.height())
		print('width:', pixmap.height())

		pixmap = pixmap.scaled(500, 300)
		self.picture.setPixmap(pixmap)

	def nextpic(self, forward=1):
		index = (App.images.index(App.activeImage))
		index = index + forward
		App.activeImage = App.images[index]
		self.setPicture()

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Settings')

	PicDisplay = PictureDisplay()
	PicDisplay.show()
	sys.exit(App.exec_())

if __name__ == "__main__":
	main()