import os
from bolt import *
from messages import *
class Search():

    #main method
    def main(self):
        filename=raw_input("Enter filename to search:\n")
        if(os.path.exists("./"+filename)):
            try:
                fm=FileManage(filename)
                x=fm.readFile()
                if(x!=False):
                    print "Search Running....<add coll animation>"
                else:
                    print "<-- x( --Error While openning File--- :-( --->"
            except():
                print "Error in openning file "+filename
                return False
        else:
            ans=raw_input("Error 404 :(\nwould you like to create a new file? :)\ny/n\n")
            if(ans.lower()=="y"):
                b=FileManage(filename)
                b.writeToFile("Hello World")
                #run a recovery mission to populate the file with the required data


s=Search()
s.main()
