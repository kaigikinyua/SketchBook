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
        #
        l=Sort()
        numFiles=len(listb4)
        self.remaining=numFiles
        print numFiles
        l=Sort()
        for item in listb4:
            l.sort(item)
        anim=threading.Thread(target=l.animation,name="anim")
        #move=threading.Thread(target=l.move,name="move",args=(listb4,))
        anim.start()
        #move.start()"""

    def move(self,destination):
        self.remaining=self.remaining-1

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
        print extension
    
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
l=Sort()
l.getDestination()

