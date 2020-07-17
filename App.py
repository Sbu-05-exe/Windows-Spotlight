import PyQt5, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QStackedWidget

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		self.Stack = QStackedWidget()
		self.mainWindow = self.createWindow()
		self.setCentralWidget(self.mainWindow)
		self.showMaximized()

	def createWindow(self):
		main_frm = QFrame(self)
		my_layout = QGridLayout()
		mainFrame.setLayout()
		return mainFrame

def main():
	App = QApplication(sys.argv)
	App.setApplicationName("Windows Spotlight Images")

	win = Window()
	win.show
	sys.exit(App.exec_())

runTests = True

def getImageinDir(dir_):
	# First check if a the file is 
	if (os.path.isdir(dir_)):
		# sifting out files with a picture file extension
		file_extensions = ['jpg','png','tiff','jpeg'] 
		images = [filename for filename in os.listdir(dir_) if (filename[len(filename) - 3:]) in file_extensions]
		if images:
			return images[0]
			
if __name__ == "__main__":
	if not(runTests):
		main()
	# else:
	# 	settings()

