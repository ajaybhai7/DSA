import os
import shutil

path = r"c:/Users/squad/Desktop/Ajay/Ajay/Practice/file.txt"

if not os.path.exists(path):
    os.mkdir(path)
    for i in range(1,101):
        file_path = os.path.join(path, f"file_{i}.txt")
        with open(file_path, "w") as f:
            pass

elif os.path.exists(path):
    print(len(os.listdir(path)))
    with open("report.txt", "w") as f:
        f.write("\n".join(os.listdir(path)))
    
else:
    print("Path does not exist.")
