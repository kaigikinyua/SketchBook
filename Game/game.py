from tkinter import *
import threading
import time
class GUI:
	def __init__(self):
		self.root=Tk()
		self.canvas=Canvas(self.root,width=100,height=100)
		self.canvas.pack()
		t1=threading.Thread(target=self.ball,name="ball")
		t2=threading.Thread(target=self.ball2,name="ball2")
		t1.start()
		t2.start()
		self.root.mainloop()
	def ball(self):
		xDisplacement=7;yDisplacement=2;
		ball=self.canvas.create_oval(10,10,15,15,fill="green")
		while(True):
			self.canvas.move(ball,xDisplacement,yDisplacement)
			ballPos=self.canvas.coords(ball)
			#xaxis of the ball
			if(ballPos[0]<0 or ballPos[2]>100):
				xDisplacement=-xDisplacement
			if(ballPos[1]<0 or ballPos[3]>100):
				yDisplacement=-yDisplacement
			time.sleep(0.05)
			self.root.update()
	def ball2(self):
		xDis=3;yDis=6;
		ball2=self.canvas.create_oval(20,20,10,10,fill="orange")
		while(True):
			self.canvas.move(ball2,xDis,yDis)
			ball2pos=self.canvas.coords(ball2)
			if(ball2pos[0]<0 or ball2pos[2]>100):
				xDis=-xDis
			if(ball2pos[1]<0 or ball2pos[3]>100):
				yDis=-yDis
			time.sleep(0.03)
			self.root.update()		
g=GUI()	
