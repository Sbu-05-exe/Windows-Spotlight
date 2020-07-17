import PyQt5, sys
from PyQt5.QtWidgets import QApplication, QWidget

class OptionsWidget(QWidget):
	def __init__(self):
		super().__init__()
		


def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Options')

	OptionWidget = OptionsWidget()
	OptionWidget.show()

	sys.exit(App.exec) 

if __name__ == '__main__':
	main()