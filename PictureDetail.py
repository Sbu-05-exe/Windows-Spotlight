import PyQt5, sys
from PyQt5.QtWidgets import QWidget, QLabel, QListWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtGui import QPixmap

class PictureDisplay(QWidget):
	def __init__(self):
		super().__init__()
		self.picture = None
		setting_layout = self.create_layout()
		self.setLayout(setting_layout)
		self.setPicture()
		self.show()

	def create_layout(self):
		self.picture = QLabel()

		hbox = QHBoxLayout()
		btnForward = QPushButton(self)
		btnBackward = QPushButton(self)

		btnForward.setSizePolicy(QP.Preferred, QP.Expanding)
		btnBackward.setSizePolicy(QP.Preferred, QP.Expanding)
		self.picture.setSizePolicy(QP.Expanding, QP.Expanding)

		btnForward.setText('-->')
		btnBackward.setText('<--')

		hbox.addWidget(btnBackward)
		hbox.addWidget(self.picture)
		hbox.addWidget(btnForward)

		return hbox

	def setPicture(self):
		pixmap = QPixmap('C:/Users/itsbu/Pictures/Wallpapers/Landscape/972941670f3f9c895c2ddbaf50e65fc608ce90e6153a40bdce13c83717942f26.jpg')
		print(dir(pixmap))
		print('height:', pixmap.height())
		print('width:', pixmap.height())

		pixmap = pixmap.scaled(500, 500)
		self.picture.setPixmap(pixmap)

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Settings')

	PictureDisplay = PictureDisplay()
	PictureDisplay.show()
	sys.exit(App.exec_())

if __name__ == "__main__":
	main()