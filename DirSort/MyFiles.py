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
    global numFiles,remaning
    def getDestination(self):
        destination=raw_input("Enter the directory to sort\n");
        listb4=os.listdir(destination)
        #
        l=Sort()
        numFiles=len(listb4)
        remaining=numFiles

        anim=threading.Thread(target=l.animation,name="anim")
        move=threading.Thread(target=l.move,name="move",args=(listb4,))
        anim.start()
        move.start()

    def animation(self):
        l=Sort()
        while True:
            sys.stdout.write(remainig+"/"+numFiles+" moved ")
            sys.stdout.flush()
            time.sleep(0.5)
            if(l.remainig==l.numFiles):
                return "Done"

    """def write(self,file)
        filen=open("b4Sort.txt","w")
        filen.write(listb4)
        filen.close()

    def sort(unsorted):
        explode(".",unsorted)

    def explode(sym,data):
        lastStr
        for char in item:
            if(char==sym):
                lastStr+=char
    """
    def move(self,destination):
        self.remaining=self.remaining-1
l=Sort()
l.getDestination()

