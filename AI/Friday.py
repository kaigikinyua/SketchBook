from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from Tkinter import * 
class Friday:
	def __init__(self):
		friday=ChatBot("Friday")
class GUI:
	def __init__(self):
		self.root=Tk()
		userPanel=Frame(self.root)
		self.chatPanel=Frame(self.root,width=200,height=400)
		scrolbar=Scrollbar(self.chatPanel)
		scrolbar.pack(side=RIGHT)
		self.chatPanel.pack(side=TOP)
		self.settingsPanel=Frame(self.root)
		settB=Button(self.settingsPanel,text="Settings",bg="green",fg="white",command=self.importList)
		settB.pack()
		self.settingsPanel.pack(side=LEFT)
		self.user=Entry(userPanel,width=30)
		self.user.pack()
		sendBtn=Button(userPanel,text="Send",bg="green",fg="white",command=self.message)
		sendBtn.pack()
		userPanel.pack(side=BOTTOM)
		self.root.mainloop()
	def message(self):
		u=self.user.get()
		l=Label(self.chatPanel,text=u,bg="lightblue")
		l.pack()
		f=ChatBot("Friday")
		r=f.get_response(u)
		rL=Label(self.chatPanel,text=r,bg="lightgreen")
		rL.pack()
	def importList(self):
		fp=open("t.txt","r")
		l=fp.readlines()
		fp.close()
		f=ChatBot("Friday")
		f.set_trainer(ListTrainer)
		f.train(l)
		done=Label(self.settingsPanel,text="Done Trainig")
		done.pack()
G=GUI()