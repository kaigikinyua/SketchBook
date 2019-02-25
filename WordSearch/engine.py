import os
from bolt import *
class Search():
    def __init__(self):
        filename=raw_input("Enter filename to search:\n")
        if(os.path.exists("./filename")):
            try:
                f=open(filename,"r")
                f.readlines();
                f.close();
            except():
                print "Error in openning file "+filename
        else:
            ans=raw_input("Error 404 :(\nwould you like to create a new file? :)\ny/n\n")
            if(ans.lower()=="y"):
                b=FileManage()
                b.writeToFile("Hello World")
s=Search()


