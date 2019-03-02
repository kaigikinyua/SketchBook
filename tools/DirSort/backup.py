import os
    #check if backup media(disk/server/Exist)
class BackUp():
    def __init__(self):
        #load settings
        try:
            f=open('settings','r')
            settings=f.readlines()
            f.close()
    #settings should be filterd to get the backup module
        except:
    #create an error module to handle file does not exist
            print "Module Unfinished"
    
    def backup(self,media):
    #infinished method
        print("unfinished backup method line")