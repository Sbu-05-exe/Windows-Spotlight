import PyQt5, os, sys
import PicOps, PictureDetail
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QMainWindow 
from PyQt5.QtWidgets import QLabel, QStackedWidget, QGridLayout

def getDirs():
	'''A function that extract paths out of a textfile'''
	
	# create empty dictionary
	dirs = {}
	with open('config.txt') as f:
		dirs_list = f.readlines()
		for item in dirs_list:
			# Add key value pairs from within the config file
			key, path = item.split('; ')
			path = path.strip()
			
			if not(path): 
				path = 'C:/'

			elif not(path[-1] == '/'):
				path = path + '/'

			dirs[key] = path

	return dirs

def getImages(dir_):
	'''A funciton that retrieves all files with an image file extension in a specific directory'''
	# First check if a the file is 
	if (os.path.isdir(dir_)):
		# sifting out files with a picture file extension
		file_extensions = ['jpg','png','tiff','jpeg']
		images = [filename for filename in os.listdir(dir_) if (filename[len(filename) - 3:]) in file_extensions]

		return images

# globals
dirs = getDirs()
images = getImages(dirs['cd'])
activeImage = images[0]

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		
		self.Stack = QStackedWidget()
		self.mainWindow, self.picOps_frm, self.picDetail_frm = self.createWindow()
		self.setCentralWidget(self.mainWindow)
		self.createMenu()
		self.show()

	def createWindow(self):
		main_frm = QFrame(self)
		# Create the layout
		grid_layout = QGridLayout()

		# Create relevant widgets
		picDetail_frm = PictureDetail.PictureDisplay()
		picOps_frm = PicOps.OptionsWidget()
		picOps_frm.setFn(picDetail_frm.setPicture)
		picOps_frm.setImages()

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

		change_curr_dir.triggered.connect(self.selectAFolder)
		change_dest_dir.triggered.connect(self.selectAFolder)

	def selectAFolder(self):
		print('hey this works')

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
	# else:
	# 	settings()