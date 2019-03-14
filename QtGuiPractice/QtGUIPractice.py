import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		#self.setWindowIcon(QtGui.QIcon('.png'))
		self.home()

		extractAction=QtGui.QAction("Quit",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave')
		extractAction.triggered.connect(self.close_app)

		self.statusBar()

		mainMenu=self.menuBar()
		fileMenu=mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

	def home(self):
		btn=QtGui.QPushButton("Quit",self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.move(50,100)
		self.show()

	def close_app(self):
		sys.exit()

def run():
	app=QtGui.QApplication(sys.argv)
	GUI=Window()
	sys.exit(app.exec_())


run() 