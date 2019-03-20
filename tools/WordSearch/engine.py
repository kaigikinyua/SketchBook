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
        lineNo=1
        s=Search()
        #search for the index of the word and the first letter of the word after the *
        if word[0]=="*":
            for myWord in fileContent:
                i=1
                while i<range(len(word)-1):
                    if word[i]!=myWord[i]:
                        if myWord[len(myWord)-1]=="\n":
                            lineNo+=1
                        break;
                    else:
                        if (len(word)-1)==i:
                            print word+" word matches with "+myWord+" at line "+str(lineNo)
                            break;
                        print myWord+" "+word[i]+" does match with "+myWord[i];
                        i+=1
        elif word[len(word)-1]=="*":
            for myWord in fileContent:
                i=0;
                while i<range(len(word)-1):
                    if word[i].lower()!=myWord[i].lower() and i<len(word)-1:
                        if myWord[len(myWord)-1]=="\n":
                            lineNo+=1
                            print myWord[i]+" does not match with "+word[i]
                        break;
                    else:
                        if (len(word)-1)==i:
                            print word+" word matches with "+myWord+" at line "+str(lineNo)
                            break;
                        i+=1
        else:
            print ":X script did not get a ' * ' :("
    #character support
    def newLineSep(self,word):
        w=""
        for i in range(len(word)):
            if (word[i]=="\n" or word[i]==" "):
                return w
            else:
                w+=word[i]
s=Search()
s.main()
