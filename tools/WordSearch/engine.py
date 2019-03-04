import os
from bolt import *
from messages import *
class Search():

    #main method
    def main(self):
        filename=raw_input("Enter filename to search:\n")
        if(os.path.exists("./"+filename)):
            try:
                #try openning the file
                fm=FileManage(filename)
                x=fm.readFile()
                if(x!=False):
                    #if the readFile method returns notFasle the file is read
                    m=Messages()
                    message=m.message("s","Reading file "+filename);
                    print message
                    #function for search
                    ans=raw_input("Enter 1 for to search for exact word or \n2 for like word\n")
                    s=Search()
                    word=raw_input("enter the word you are searching for\n>")
                    if ans==str("1"):
                        #pass the fileContent to the exactword function you would like to search for
                        s.exactWord(x,word)
                    else:
                        print "Add * to the letters you would like to skip/dont know"
                        s.likeWord(x,word)
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
    def likeWord(self,fileContent,word):
        lineNo=0
        s=Search()
        for line in fileContent:
            #search for the index of the word and the first letter of the word after the *
            if word[0]!="*":
                x=s.newLineSep(line);
                i=1;
                for letter in x:
                    if word[i]==x[i]:
                        i+=1
                        if(len(x)==i):
                            return True
                    else:
                        break;
            elif word[len(word)-1]=="*":
                #search for the words starting from the beginnning
                x=s.newLineSep(line)
                i=0
                for letter in x:
                    if word[i]==x[i]:
                        i+=1
                        if(len(x)==(i+1)):
                            return True
                    else:
                        break;
            else:
                print ":( Appication Broken :x "+word
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
