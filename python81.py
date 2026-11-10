# Os Module
import os
if not os.path.exists("my folder"):
    os.mkdir("my folder")
    print("folder created")
else:
    print("folder already exists")
current_files = os.listdir("my folder")
print("current files in my folder:",current_files)
