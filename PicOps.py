import PyQt5, sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton
from PyQt5.QtWidgets import QListWidget, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtCore import Qt

def getImages(dir_):
	# First check if a the file is 
	if (os.path.isdir(dir_)):
		# sifting out files with a picture file extension
		file_extensions = ['jpg','png','tiff','jpeg'] 
		images = [filename for filename in os.listdir(dir_) if (filename[len(filename) - 3:]) in file_extensions]
		
		return images

class OptionsWidget(QWidget):
	def __init__(self, dirs = None, setImageFunc = None):
		super().__init__()
		# Widgets that we will repeatedly make reference to 
		self.layout = None
		self.QListWidget = None

		# A dictionary that helps our function flow
		self.dirs = dirs
		self.initUI()
		self.setLayout(self.layout)
		self.show()

	def initUI(self):
		grid_layout = QGridLayout()
		btn_layout = QVBoxLayout() 

		btn_frame = QFrame()
		btn_frame.setLayout(btn_layout) 

		self.QListWidget = QListWidget()

		btnMove = QPushButton()
		btnCopy = QPushButton()
		btnStart = QPushButton()
		btnDelete = QPushButton()

		btnMove.setText('Move to ')
		btnCopy.setText('Copy to ')
		btnStart.setText('Start')
		btnDelete.setText('Delete')

		btnMove.setSizePolicy(QP.Preferred, QP.Preferred)
		btnCopy.setSizePolicy(QP.Preferred, QP.Preferred)
		btnStart.setSizePolicy(QP.Preferred, QP.Preferred)
		btnDelete.setSizePolicy(QP.Preferred, QP.Preferred)

		# btnMove.clicked.connect()
		# btnCopy.clicked.connect()

		lblRoot = QLabel()
		lblRoot.setText('Root Label')
		lblRoot.setAlignment(Qt.AlignCenter)
		# print(dir(lblRoot.alignment))
		# print(dir(lblRoot))

		btn_layout.addWidget(btnCopy)
		btn_layout.addWidget(btnMove)
		btn_layout.addWidget(btnStart)
		btn_layout.addWidget(btnDelete)

		grid_layout.addWidget(lblRoot)
		grid_layout.addWidget(self.QListWidget,1,0)
		grid_layout.addWidget(btn_frame, 1 , 1 )

		self.layout = grid_layout

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Options')

	PicItems = OptionsWidget()
	PicItems.show()

	sys.exit(App.exec_()) 

if __name__ == '__main__':
	main()