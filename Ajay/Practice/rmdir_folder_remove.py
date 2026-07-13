import os

for i in range(1, 100):
    folder_path = f"data"
    try:
        os.rmdir(folder_path)
        print(f"Successfully removed the folder:{folder_path}")
        break
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")