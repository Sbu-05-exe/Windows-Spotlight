import PyQt5, os, sys
import PicOps, PictureDetail
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QMainWindow 
from PyQt5.QtWidgets import QLabel, QStackedWidget, QGridLayout
from PyQt5.QtWidgets import QFileDialog

def getDirs():
	'''A function that extract paths out of a textfile'''
	
	# create empty dictionary
	paths = {}

	default_dir = os.getcwd() + '\\files'
	# default_dir = input(os.system('cd')) + '/files'

	with open('config.txt') as f:
		path_lst = f.readlines()

		for item in path_lst:
			# Add key value pairs from within the config file
			key, path = None, None

			split_line = item.split(';')
			if len(split_line) == 2:
				key, path = split_line[0].strip(), split_line[1].strip()
			
			if key:
				if not(path) or path == '\n': 
					path = default_dir

				paths[key] = path
	
	return paths

def getImages(dir_):
	'''A funciton that retrieves all files with an image file extension in a specific directory'''
	# First check if a the file is
	if (os.path.isdir(dir_)):
		# sifting out files with a picture file extension
		file_extensions = ['jpg','png','tiff','jpeg']
		images = [filename for filename in os.listdir(dir_) if (filename[len(filename) - 3:]) in file_extensions]

		images = [filename for filename in images if os.path.getsize(paths['cd'] + '\\' + filename) > 150000 ]
		
		return images

	return []

def setup():
	'''Initial setup for the applicaiton. Store and look for files here by default'''
	if not('files' in os.listdir()):
		os.mkdir('files')

# globals

paths = getDirs()
images = getImages(paths['cd'])
activeImage = images[0] if images else None

setup()

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		
		self.Stack = QStackedWidget()
		self.mainWindow, self.picOps_frm, self.picDetail_frm = self.createWindow()
		self.picOps_frm.setImages(images)
		self.setCentralWidget(self.mainWindow)
		self.createMenu()
		self.show()

	def createWindow(self):
		global images, activeImage
		main_frm = QFrame(self)
		# Create the layout
		grid_layout = QGridLayout()

		# Create relevant widgets
		picDetail_frm = PictureDetail.PictureDisplay(activeImage, images, paths['cd'])
		picOps_frm = PicOps.OptionsWidget(self.setPixmap, self.updateImages, paths)

		# Add them to layout
		grid_layout.addWidget(picDetail_frm)
		grid_layout.addWidget(picOps_frm)

		# set layout and return componet
		main_frm.setLayout(grid_layout)
		return main_frm, picOps_frm, picDetail_frm

	def createMenu(self):
		menu = self.menuBar()
		file = menu.addMenu('file')
		change_curr_dir = file.addAction('Change current directory')
		change_dest_dir = file.addAction('Change destination directory')

		change_curr_dir.triggered.connect(lambda: self.selectAFolder('cd'))
		change_dest_dir.triggered.connect(lambda: self.selectAFolder('dest_dir'))

	def selectAFolder(self, key = 'cd'):
		# print('hey this works')
		global paths, images
		folder = str(QFileDialog.getExistingDirectory(self, "SelectDirectory", paths['cd']))

		paths[key] = folder
		self.picOps_frm.setPaths(paths)

		if key == 'cd':
			self.picDetail_frm.setPath(folder)
			images = getImages(folder)
			self.picOps_frm.setFolder(folder)
			self.picOps_frm.setImages(images)

	def setPixmap(self, actImgs):
		global activeImage

		activeImage = actImgs

		self.picDetail_frm.setActiveImage(activeImage)
		self.picDetail_frm.setPicture()

	def closeEvent(self, event):
		global paths

		# Save the current state of all directories into config file
		with open('config.txt', 'w') as f:
			data = [key + '; ' + paths[key] for key in paths.keys()]
			f.write('\n'.join(data))

def main():
	App = QApplication(sys.argv)
	App.setApplicationName("Windows Spotlight Images")

	win = Window()
	win.show
	sys.exit(App.exec_())


runTests = False
	
if __name__ == "__main__":	
	if not(runTests):
		main()