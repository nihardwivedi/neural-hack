'''
Name of the Task : Messy Folder
KIITFEST ID : KF36723
Operating System : MacOS Sierra
Programming Language used: Python
External modules used (if any) : os,sys
Additional instructions to use the program (if any) : The files to be organized must exist in current working directory.
'''
#!/usr/bin/python
# Traverse all of the files in the given directory and move
# them into subfolders based on their extension type.
import os
import sys
path1 = os.getcwd()
print path1
if __name__ == '__main__':
    # Define the folder names for each extension type here
    folderNames = {".txt" : "txt",
                   ".csv" : "csv",
                   ".mp3" : "mp3"}

     
    # NOTE: Assuming files in current folder
    directory = "./"
    files = os.listdir(directory)

    # Traverse all of the files
    for filename in files:
        # Grab the extension of the file
        extension = os.path.splitext(filename)[1]
        
        if extension in folderNames:
            # Grab the folder where this file should be stored
            folder = os.path.join(directory, folderNames[extension])

            # Create the folder if it does not already exist
            if not os.path.exists(folder):
                os.mkdir(folder)
                
            # Move the file into the folder
            os.rename(os.path.join(directory, filename),
            os.path.join(folder, filename))
