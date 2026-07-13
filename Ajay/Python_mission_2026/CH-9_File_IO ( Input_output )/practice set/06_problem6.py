''' Write a program to mine a log file and find out whether
it contains "python" '''

with open("log.txt", "r") as f:
    file = f.read()
if "python" in file:
    print("Yes Python is present")

else:
    print("python is not present")