def myFunc():
    print("Hello World!")

if __name__ == "__main__":
    myFunc()
    print(__name__) # print name of file if we import anywhere 
    print("We are directly running this code")
#Output: 
#Hello World!
#__main__