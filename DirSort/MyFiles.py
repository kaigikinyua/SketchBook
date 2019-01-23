import glob
import threading
import time
import os
import sys
#procedure 
"""
    1.list * the files and folders in the directory to be sorted
    2.get media files ,pdfs,images,code etc
    3.list * these details in a file
    4.user selects which directory to move them to
    5.move the files record where the files have been moved to 
    6.animation thread to prevent canceling
"""
class Sort:
    numFiles=0;
    def getDestination(self):
        destination=raw_input("Enter the directory to sort\n");
        listb4=os.listdir(destination)
        l=Sort()
        numFiles=len(listb4)
        self.remaining=numFiles
        print numFiles
        return destination
        #l=Sort()
        #for item in listb4:
         #   l.sort(item)
        #anim=threading.Thread(target=l.animation,name="anim")
        #move=threading.Thread(target=l.move,name="move",args=(listb4,))
        #anim.start()
        #move.start()"""

    def move(self):
        l=Sort()
        settings=l.loadSettings()
        listb4=l.getDestination()
        os.chdir(listb4)
        if (settings!=False):
            for i in range(len(settings)):
                #l.fileFormat(settings[i])
                print settings

    def animation(self):
        l=Sort()
        total=20;counter=0;i=0;
        anim=['|','/','-','\\']
        while (counter<=total):
            sys.stdout.write("\r"+str(counter)+"/"+str(total)+" moved "+anim[i])
            time.sleep(0.5)
            counter+=1;i+=1;
            sys.stdout.flush()
            if(i>3):
                i=0;
        sys.stdout.write("\n")

    def sort(self,item):
        l=Sort()
        extension=l.explode(item)
        #f=open("settings","r")
        #settings=f.readlines()
        #f.close()
        #creating the format 
        #l.move(item)
        #print extension
    
    def explode(self,name):
        l=len(name)
        i=0;dot=l-1;ext="";
        for i in range(l-1):
            if(name[dot]!="."):
                ext+=name[dot]
                dot-=1
        extension=""
        i=len(ext)-1
        while(i>=0):
            extension+=ext[i]
            i-=1
        return extension

    def loadSettings(self):
        try:
            f=open("settings","r")
            settings=f.read().split("\n")
            f.close()
            print "Settings loaded automatically "+settings
            return settings
        except:
            ans=raw_input("You do not have an automatic configration\n\nWould you like to set up one?\n\ny/n\n")
            ans=ans.lower()
            if ans=="y":
                f=open("settings","w")
                quit=False
                while(quit!=True):
                    extensions=raw_input("enter the file extension(s) (placing  a . after each if they are many)\n")
                    destination=raw_input("Enter the absolute directory where you would like to place these files\n")
                    if(os.path.isdir(destination)==True):
                        #start execution
                        f.write(extensions+"["+destination+"]"+"\n")
                        ansquit=raw_input("Add another extension? y/n\n")
                        ansquit=ansquit.lower()
                        if(ansquit=="n"):
                            quit=True
                            f.close()
                            f=open("settings","r")
                            self.settings=f.readlines()
                            f.close()
                            return self.settings
                    else:
                        print("The path you specified is either not a directory or does not exist\n")

            elif ans=="n":
                #should start executing but the user will have to enter directories manually
                return False
                
            else:
                print("Please enter y/n")
                l=Sort()
                l.loadSettings()

    def fileFormat(self,settings):
        print "Hello"

    """ def fileFormat(self,sett):
        path=""
        finalSett=[]
        temp=""
        for i in range(len(sett)-1):
            if(sett[i]!="." or sett[i]!="[" or sett[i]!="]"):
                temp+=sett[i]
            elif(sett[i]=="."):
                finalSett+=[temp]
                print temp
                temp=""
            elif(sett[i]=="["):
                temp=""
                while(i<=len(sett)-1 and sett[i]!="]" and sett[i]!="\n"):
                    temp+=sett[i]
                    i+=1
                path=temp
                print path
                finalSett+=[path]
            else:
                print "Error"
                """
l=Sort()
l.move()
#l.loadSettings()