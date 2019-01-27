#used to filter the data entered into the program
import os
class Filter():
    def checkDir(self,dir):
        if(os.path.isdir(dir)==True):
            return True
        else:
            return False
    
    def enterDir(self):
        dir=raw_input("Enter Directory\n")
        return dir
    
    def extension(self,ext):
        #move the extension to the directory
        print("Hello")
    def history(self,destination,former):
        d=os.listdir(destination)
        f=open("destination","w")
        f.write(d)
        f.close()
        f=open("former","w")
        f.write(os.listdir(former))
        f.close()

