import sys
import os
from PyQt4 import QtGui,QtCore
import cv2
from PIL import Image
import numpy as np
import sqlite3

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("Chena Manush")
		self.setWindowIcon(QtGui.QIcon('logo.png'))
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
		btnRecognize=QtGui.QPushButton("Recognize Face",self)
		btnTakePictures=QtGui.QPushButton("Take Pictures",self)
		btnTrainData=QtGui.QPushButton("Train Dataset",self)
		btnStop=QtGui.QPushButton("Quit Window",self)
		btnRecognize.clicked.connect(self.recognize_face)
		btnTakePictures.clicked.connect(self.take_pictures)
		btnTrainData.clicked.connect(self.train_data)
		btnStop.clicked.connect(self.close_app)
		btnRecognize.move(350,75)
		btnTakePictures.move(350,125)
		btnTrainData.move(350,175)
		btnStop.move(350,225)
		self.show()

	def close_app(self,crashed):
		print("in the loop")
		crashed=True
		#sys.exit()


	#function for taking pictures
	def take_pictures(self):
		def insertOrUpdate(ID,Name):
			conn=sqlite3.connect("faceBase.db")
			cmd="SELECT * FROM People WHERE ID="+str(ID)
			cursor=conn.execute(cmd)
			isRecordExist=0
			for row in cursor:
				isRecordExist=1
			if(isRecordExist==1):
				cmd="UPDATE People SET Name="+str(Name)+"WHERE ID="+str(ID)
			else:
				cmd="INSERT INTO People(ID,Name) Values(?,?)",("+str(ID)","+str(Name)")
			conn.execute(cmd)
			conn.commit()
			conn.close()

		id=input('enter User Id: ')
		name=input('enter your name: ')
		insertOrUpdate(id,name)
		faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		cam=cv2.VideoCapture(0);
		sampleNum=0;
		while(True):
			ret,img=cam.read();
			gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			faces=faceDetect.detectMultiScale(gray,1.3,5);
			for(x,y,w,h) in faces:
				sampleNum=sampleNum+1;
				cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				cv2.waitKey(100)
			cv2.imshow("Face",img)
			if(sampleNum>20):
				break;
		cam.release()
		cv2.destroyAllWindows()

	def train_data(self):
		recognizer=cv2.face.createLBPHFaceRecognizer();
		path='dataSet'

		def getImagesWithID(path):
			imagePaths=[os.path.join(path,f)for f in os.listdir(path)]
			faces=[]
			IDs=[]
			for imagePath in imagePaths:
				faceImg=Image.open(imagePath).convert('L');
				faceNp=np.array(faceImg,'uint8')
				ID=int(os.path.split(imagePath)[-1].split('.')[1])
				faces.append(faceNp)
				print (ID)
				IDs.append(ID)
				cv2.imshow("training",faceNp)
				cv2.waitKey(10)
			return np.array(IDs),faces

		Ids,faces=getImagesWithID(path)
		recognizer.train(faces,Ids)
		recognizer.save('recognizer/trainingData.yml')
		cv2.destroyAllWindows()


	def showImg(self,img):
		cv2.imshow('img',img)

	def recognize_face(self):
		print('working finally')
		#function for getting image from Database
		def getProfile(id):
			conn=sqlite3.connect("faceBase.db")
			cmd="SELECT *FROM People WHERE ID="+str(id)
			cursor=conn.execute(cmd)
			profile=None
			for row in cursor:
				profile=row
			conn.close()
			return profile
		faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		cam=cv2.VideoCapture(0);
		recognizer=cv2.face.createLBPHFaceRecognizer()
		recognizer.load("recognizer\\trainingData.yml")
		font=cv2.FONT_HERSHEY_SIMPLEX
		id=0
		sampleNum=0;
		crashed=False
		while not crashed:
			ret,img=cam.read();
			gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			faces=faceDetect.detectMultiScale(gray,1.6,5)
			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				id,conf=recognizer.predict(gray[y:y+h,x:x+w])
				profile=getProfile(id)
				if(profile!=None):
					cv2.putText(img,profile[1],(x,y+h+50),font,1,(255,255,200),2,cv2.LINE_AA); 
			self.showImg(img)
			cv2.waitKey(100)
			if cv2.waitKey(30)& 0xff==ord('q'):
				break

		cam.release()
		cv2.destroyAllWindows()
def run():
	app=QtGui.QApplication(sys.argv)
	GUI=Window()
	sys.exit(app.exec_())


run() 
