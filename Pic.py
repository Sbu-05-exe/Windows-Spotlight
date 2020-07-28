import PyQt5, os, sys, utility
from PyQt5.QtWidgets import QWidget, QFrame, QApplication, QPushButton, QLabel
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt5.QtWidgets import QSizePolicy as QP
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class PicWidget(QWidget):
	def __init__(self, *args, **kwargs):
		super(PicWidget, self).__init__(*args, **kwargs)
		# TODO:
		self.paths = utility.getPaths()
		self.images = utility.getImages(self.paths['cd'])
		self.activeImage = self.images[0] if self.images else None

		self.createPicDisplay()
		self.createPicOp()
		self.setImages()
		self.show()
		self.initUI()
		'''
====================================================================================
				Setters and getters (mutators and accessors)
====================================================================================		
		'''

	def setPath(self, key, path):
		self.paths[key] = path

	def getPath(self):
		return self.paths['cd']

	def updateCD(self, folder):
		self.lblRoot.setText(folder)
		self.images = utility.getImages(folder)
		self.activeImage = self.images[0] if self.images else None
		self.setImages()

		'''
====================================================================================
						Picture Display
====================================================================================
		'''

	def createPicDisplay(self):
		self.pixmap = QLabel()

		hbox = QHBoxLayout()

		btnForward = QPushButton(self)
		btnBackward = QPushButton(self)

		# Make widgets reponsive

		btnForward.setSizePolicy(QP.Preferred, QP.Expanding)
		btnBackward.setSizePolicy(QP.Preferred, QP.Expanding)
		self.pixmap.setSizePolicy(QP.Expanding, QP.Expanding)

		btnForward.setText('-->')
		btnBackward.setText('<--')

		btnForward.clicked.connect(lambda x: self.nextpic(1))
		btnBackward.clicked.connect(lambda x: self.nextpic(-1))

		hbox.addWidget(btnBackward)
		hbox.addWidget(self.pixmap)
		hbox.addWidget(btnForward)


		picDisplay = QFrame()
		picDisplay.setLayout(hbox)

		self.Pic_frm = picDisplay 
		self.btnBackward = btnBackward
		self.btnForward = btnForward

		return btnBackward, btnForward

	def nextpic(self, forward=1):
		index = (self.images.index(self.activeImage))
		index = index + forward

		if len(self.images) > 1:
			index = index % len(self.images)
			self.activeImage = self.images[index]
			self.setPixmap()

		else:
			self.pixmap.setText('No more file')

		'''
====================================================================================
						Picture Operation
====================================================================================
		'''

	def createPicOp(self):

		grid_layout = QGridLayout()
		btn_layout = QVBoxLayout()

		btn_frame = QFrame()
		btn_frame.setLayout(btn_layout) 

		self.pic_lst = QListWidget()
		# TODO
		self.pic_lst.itemClicked.connect(self.onItemSelect)

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

		# TODO
		btnMove.clicked.connect(self.onMoveClick)
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

		PicOpt_frm = QFrame()
		PicOpt_frm.setLayout(grid_layout)

		self.Option_frm = PicOpt_frm

	def setImages(self):
		self.pic_lst.setEnabled(True)
		self.pic_lst.clear()
		self.pic_lst.addItems(self.images)

		if self.images:
			# Automatically select the first item in the list if there is 1
			# self.setPixmap()
			pass

		else:
			self.pic_lst.addItem('This directory does not contain images.')
			self.pic_lst.addItem('Change direcotories to continue')
			self.pic_lst.setEnabled(False)

	def onItemSelect(self, item):
		self.activeImage = item.text()
		self.setPixmap()

	def setPixmap(self):
		if self.activeImage:
			# set the picture on the screen

			src = self.paths['cd'] + '/' + self.activeImage

			pixmap = QPixmap(src)
			height, width = pixmap.height(), pixmap.width()

			pixmap = pixmap.scaled(500, 300)
			self.pixmap.setPixmap(pixmap)

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
			print('Disabling button')
			self.btnForward.setEnabled(False)
			self.btnBackward.setEnabled(False)

	def onMoveClick(self,):
		cd = self.paths['cd']
		src = cd + '/' + self.activeImage if '/' in cd else src + '\\' + self.activeImage
		dest = self.paths['destdir']
		os.chdir(cd)

		# First check if the file is in the destination folder
		if not(self.activeImage in os.listdir(dest)):
			# print('moving folders')
			print('moving...')
			command = f'move "{self.activeImage}" "{dest}"'
			os.system(command)
		else:
			# print('already exists in that folder')
			print('ActiveImage already exists in dests')
			command = f'del "{self.activeImage}"'
			os.system(command)

		image = self.activeImage
		self.nextpic()
		self.images.remove(image)
		self.pic_lst.clear()
		self.pic_lst.addItems(self.images)

	def onCopyClick(self):
		dest = self.paths['desdir']
		
		os.system(f'type "{src}"" > "{src}1" ')
		os.system(f'move "{src}"1 "{desdir}" ')
		os.system(f'ren "{src}"1 "{src}"')

	def onStartClick(self):
		home = self.paths['home']
		os.chdir(home)
		os.startfile('spotlight.bat')
		self.setImages()

	def onDelClick(self):
		cd = self.paths['cd']
		os.chdir(cd)
		os.system(f'del {self.activeImage}')
		print(f'deleting {self.activeImage}...')
		self.nextpic()

	def initUI(self):
		grid_layout = QGridLayout()

		grid_layout.addWidget(self.Pic_frm)
		grid_layout.addWidget(self.Option_frm)

		self.setLayout(grid_layout)

	def closeEvent(self,event):
		os.chdir(self.paths['home'])

		# Save the current state of all directories into config file
		with open('config.txt', 'w') as f:
			data = [key + ';' + self.paths[key] for key in self.paths.keys()]
			f.write('\n'.join(data))

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('PicPy')

	wn = PicWidget()
	wn.show()
	sys.exit(App.exec_())

if __name__ == "__main__":
	main()