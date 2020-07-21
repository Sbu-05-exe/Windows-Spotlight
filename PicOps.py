import PyQt5, sys, os
import App
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton
from PyQt5.QtWidgets import QListWidget, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtCore import Qt

class OptionsWidget(QWidget):
	def __init__(self, setImageFunc = None):
		super().__init__()
		# Widgets that we will repeatedly make reference to 
		self.layout = None
		self.pic_lst = None

		self.initUI()
		self.setLayout(self.layout)
		self.show()

	def setImages(self):
		if App.dirs:
			cd = App.dirs['cd']
			self.pic_lst.addItems(App.images)

			if App.images:
				# Automatically select the first item in the list if there is 1
				self.onItemSelect(self.pic_lst.item(0))

	def initUI(self):
		grid_layout = QGridLayout()
		btn_layout = QVBoxLayout()

		btn_frame = QFrame()
		btn_frame.setLayout(btn_layout) 

		self.pic_lst = QListWidget()
		self.pic_lst.itemClicked.connect(self.onItemSelect)
		self.pic_lst.itemActivated.connect(self.onItemSelect)
		# print(dir(self.pic_lst))

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

		cd = App.dirs['cd'] if App.dirs else ''
		lblRoot = QLabel()
		lblRoot.setText(f'Current folder: {cd}')
		lblRoot.setAlignment(Qt.AlignCenter)
		# print(dir(lblRoot.alignment))
		# print(dir(lblRoot))

		btn_layout.addWidget(btnCopy)
		btn_layout.addWidget(btnMove)
		btn_layout.addWidget(btnStart)
		btn_layout.addWidget(btnDelete)

		grid_layout.addWidget(lblRoot)
		grid_layout.addWidget(self.pic_lst,1,0)
		grid_layout.addWidget(btn_frame, 1 , 1 )

		self.layout = grid_layout

	def onItemSelect(self, item):
		App.activeImage = item.text()

		self.setPixmap()


	def setFn(self, fn):
		self.setPixmap = fn

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Options')

	PicItems = OptionsWidget()
	PicItems.show()
	PicItems.setImages()

	sys.exit(App.exec_()) 

if __name__ == '__main__':
	main()