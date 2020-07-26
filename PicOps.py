import PyQt5, sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton
from PyQt5.QtWidgets import QListWidget, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtCore import Qt

temp_func = lambda x : None

class OptionsWidget(QWidget):
	def __init__(self, fnPixmap = temp_func, fnUpdate = temp_func, paths = None):
		super().__init__()
		# Default will be a function that returns none, so my program hopefully won't break
		self.setPixmap, self.updateApp, self.paths = fnPixmap, fnUpdate, paths

		# Widgets that we will repeatedly make reference to 
		self.layout = None
		self.pic_lst = None

		self.initUI()
		self.setLayout(self.layout)
		self.show()

	def setImages(self, images):
		self.pic_lst.setEnabled(True)
		self.pic_lst.clear()
		self.pic_lst.addItems(images)

		if images:
			# Automatically select the first item in the list if there is 1
			self.onItemSelect(self.pic_lst.item(0))

		else:
			self.pic_lst.addItem('This directory does not contain images.')
			self.pic_lst.addItem('Change direcotories to continue')
			self.pic_lst.setEnabled(False)


	def initUI(self):
		grid_layout = QGridLayout()
		btn_layout = QVBoxLayout()

		btn_frame = QFrame()
		btn_frame.setLayout(btn_layout) 

		self.pic_lst = QListWidget()
		self.pic_lst.itemClicked.connect(self.onItemSelect)
		self.pic_lst.itemActivated.connect(self.onItemSelect)

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

		btnStart.clicked.connect(self.onStartClick)

		cd = self.paths['cd'] if self.paths else ''
		lblRoot = QLabel()
		lblRoot.setText(f'Current folder: {cd}')
		lblRoot.setAlignment(Qt.AlignCenter)

		self.lblRoot = lblRoot

		btn_layout.addWidget(btnCopy)
		btn_layout.addWidget(btnMove)
		btn_layout.addWidget(btnStart)
		btn_layout.addWidget(btnDelete)

		grid_layout.addWidget(lblRoot)
		grid_layout.addWidget(self.pic_lst,1,0)
		grid_layout.addWidget(btn_frame, 1 , 1 )

		self.layout = grid_layout

	def onStartClick(self):
		os.startfile('spotlight.bat')
		self.updateApp()

	def onMoveClick(self):
		self.active

	def onItemSelect(self, item):
		self.setPixmap(item.text())


	def setFolder(self, folder):
		self.lblRoot.setText(folder)

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Options')

	PicItems = OptionsWidget()
	PicItems.show()
	PicItems.setImages([])

	sys.exit(App.exec_()) 

if __name__ == '__main__':
	main()