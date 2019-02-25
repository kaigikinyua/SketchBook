filename =""
class FileManage():
    def __init__(self):
        global filename
        filename=raw_input("Enter the filename");
        unwanted=[" ","."];
        if(len(filename)>0):
            for un in unwanted:
                if filename==un:
                    print "file cannot be named '"+filename+"' \nplease try again"
                    c=FileManage()
        else:
            print "Filename cannot be empty"
            c=FileManage()

#create file with the filename
    def createFile(self):
        try:
            f=open(filename,"w")
            f.close()
        except():
            print "Error in creating file"
#append text to the end
    def appendToFile(self,text):
        try:
            f=open(filename,"r")
            content=f.readlines()
            f.close()
            content+=[text]
            #add a catchblock to catch dennied write permissions
            f=open(filename,"w")
            f.write(content)
            f.close()
        except():
             print "Error in opening the filename"+filename

    def preAppend(self,text):
        try:
            f=open(filename,"r")
            content=f.readlines()
            f.close()
            content+=text
            newWrite=[];i=len(content)-1;
            for item in content:
                newWrite+=[content[i]]
                i-=1
            #add a catchblock to indicate dennied write permissions
                f=open(filename,"w")
                f.write(newWrite);
                f.close()
        except:
            print "Error in preappending to file"

    def writeToFile(self,text):
        try:
            f=open(filename,"w");
            f.write(text)
            f.close()
        except():
            print "Error in creating the file"
