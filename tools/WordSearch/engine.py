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
                    m=Messages()
                    message=m.message("s","Reading file "+filename);
                    print message
#function for search
                    word=raw_input("enter the word you are searching for\n>")
                    s=Search()
                    s.exactWord(x,word)
                else:
                    m=Messages()
                    message=m.message("f","Reading file "+filename);
                    print message
            except():
                m=Messages()
                message=m.message("f","Opening file "+filename);
                print message
        else:
            ans=raw_input("Error 404 :(\nwould you like to create a new file? :)\ny/n\n")
            if(ans.lower()=="y"):
                b=FileManage(filename)
                if(b.writeToFile("Hello World")!=True):
                    m=Messages()
                    message=m.message("f","Opening file "+filename);
                    print message
                else:
                    m=Messages()
                    message=m.message("s","Writing to file "+filename);
                    print message

    #search engine -- vroom
    def exactWord(self,fileContent,search):
        lineNo=0
        s=Search()
        for line in fileContent:
            if s.newLineSep(line.lower())==search.lower():
                print lineNo+1
                break
            else:
                lineNo+=1
    #def likeWord(self):

    #character support
    def newLineSep(self,word):
        w=""
        for i in range(len(word)):
            if (word[i]=="\n" or word[i]==" " or word[i]=="."):
                return w
            else:
                w+=word[i]
s=Search()
s.main()
