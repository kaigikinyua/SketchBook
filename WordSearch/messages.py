class Messages():
    def __init__(self,state,message):
        #sucess
        if (state.lower()=="s"):
            print (message+" done :)")
        else:
            print (message+" failed x(")
