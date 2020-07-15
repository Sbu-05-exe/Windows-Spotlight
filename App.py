import PyQt5, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame,QLabel, QStackedWidget

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

if __name__ == "__main__":
	main()

