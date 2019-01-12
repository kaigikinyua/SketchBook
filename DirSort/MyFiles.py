import os
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
    def getDestination(self):
        destination=raw_input("Enter the directory to sort\n");
        listb4=os.listdir(self.destination)
        #file write
        write("b4sort")
        sort(listb4)
        move(destination)

    def write(self,file)
        filen=open("b4Sort.txt","w")
        filen.write(listb4)
        filen.close()

    def move(destination):
        os.mo
        
    def sort(unsorted):
        explode(".",unsorted)
        
    def explode(sym,data):
        lastStr
        for char in item:
            if(char==sym):
                lastStr+=char


