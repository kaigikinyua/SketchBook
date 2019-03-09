import glob
import threading
import time
import os
import sys
import shutil
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
        if(os.path.isdir(destination)):
            return destination
        else:
            print destination+" :X is not a recognised directory\nRetry"
            l=Sort()
            l.getDestination();
    def destinationList(self,destination):
        listb4=os.listdir(destination)
        numFiles=len(listb4)
        return listb4

    def move(self):
        l=Sort()#instatiate the class Sort to use its methods
        settings=l.loadSettings()#load setting from the settings file
        fromDest=l.getDestination()#directory which needs to be sorted
        listb4=l.destinationList(fromDest)#list the files in the list to be sorted --> should create a file with the files before being sorted
        allienFiles=[]
        percentage=0
        print len(listb4)
        if (settings!=False):#if setting were not detected
            for i in range(len(settings)-1):
                settExt=settings[i].split(".")#split the ith setting to get the extension
                settBound=0#???
                for k in range(len(settExt)-1):
                    #print moving *.whatever to dir..
                    #animation to show the user the completed tasks
                    for j in range(len(listb4)-1):
                        x=listb4[j].split(".")
                        #sys.stdout.flush()
                        #print fromDest+" to "+str(settExt[len(settExt)-1])
                        anim=['|','/','-','\\']
                        if(j<len(listb4)):
                            percentage=(j*100)/float(len(listb4));
                            sys.stdout.write("\r"+str(round(percentage,1))+"'%'Copied "+int((percentage)/10)*"|")
                        else:
                            #should get an array that acounts for  the noumber of Copied files
                            sys.stdout.write("\r Done sorting "+str(len(listb4))+"\n")
                        try:
                            if x[1]==settExt[k]:
                                shutil.copy(fromDest+"/"+str(listb4[j]),settExt[len(settExt)-1])
                                x[j]=="Done"
                                time.sleep(1)
                            #else:
                            #    print "Error in copying "+fromDest+"/"+str(listb4[j])+" to "+str(settExt[len(settExt)-1])
                        except:
                            #print "File "+str(listb4[j])+" does not have an extension"
                            allienFiles+=[listb4[j]]
                            time.sleep(0.5)
                            i=0
        #else enter a dirctory to move the files into
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
            print "Settings loaded automatically "
            print settings
            return settings
        except:
            ans=raw_input("-----ERROR----\nYou do not have an automatic configration\n\nWould you like to set up one?\n\ny/n\n")
            ans=ans.lower()
            if ans=="y":
                f=open("settings","w")
                quit=False
                while(quit!=True):
                    extensions=raw_input("enter the file extension(s) (placing  a . after each if they are many)\n")
                    destination=raw_input("Enter the absolute directory where you would like to place these files\n")
                    if(os.path.isdir(destination)==True):
                        #start execution
                        f.write(extensions+"."+destination+"\n")
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

l=Sort()
l.move()
#l.loadSettings()
