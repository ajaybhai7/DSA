import os
import shutil

path = "c:/Users/squad/Desktop/Ajay/Ajay/Practice/data"

if os.path.exists(path):
    shutil.rmtree(path)
    print(f"folder deleted successfully.")

else:
    os.mkdir(f"{path}")
    
    
    for i in range(1,101):
        os.mkdir(f"{path}/Day{i}")
    
    print(f"folder created successfully.")

