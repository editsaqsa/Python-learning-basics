# Exercise 7 project
import os 
folder_path = "clutter_folder"

files = os.listdir(folder_path)

i = 1

for file in files:

    if file.endswith(".png"):

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, f"{i}.png")

        os.rename(old_path, new_path)

        print(f"Rename: {file} to {i}.png")
        