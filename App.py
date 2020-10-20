import PyQt5, os, sys
import Pic
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QMainWindow 
from PyQt5.QtWidgets import QLabel, QStackedWidget, QGridLayout
from PyQt5.QtWidgets import QFileDialog

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		 
		# Widgets
		self.Stack = QStackedWidget()
		self.main_frm = Pic.PicWidget()
		self.Stack.addWidget(self.main_frm)

		# Layout
		self.setGeometry(400, 200, 500 ,500)
		self.setCentralWidget(self.Stack)
		self.createMenu()
		self.show()

	def createMenu(self):
		menu = self.menuBar()
		file = menu.addMenu('file')
		
		cd = os.path.basename(self.main_frm.getPath())
		destpath = os.path.basename(self.main_frm.getDestPath())

		change_curr_dir = file.addAction(f"Change current directory \t| {cd}" )
		change_dest_dir = file.addAction(f"Change destination directory \t| {destpath} ")

		change_curr_dir.triggered.connect(lambda: self.selectAFolder('cd'))
		change_dest_dir.triggered.connect(lambda: self.selectAFolder('destdir'))

	def selectAFolder(self, key = 'cd'):
		# print('hey this works')
		destpath = self.main_frm.getDestPath()
		folder = str(QFileDialog.getExistingDirectory(self, "SelectDirectory", destpath))

		self.main_frm.setPath(key, folder)

		if key == 'cd':
			self.main_frm.updateCD(folder)

	def closeEvent(self, event):
		self.main_frm.closeEvent(event)

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