import os
import shutil
from tkinter import Tk, filedialog

# Main window hide
root = Tk()
root.withdraw()

# Folder select karo
folder = filedialog.askdirectory(title="Select Folder to Delete")

if folder:
    try:
        shutil.rmtree(folder)
        print("Folder deleted successfully!")
    except Exception as e:
        print("Error:", e)
else:
    print("No folder selected.")