import os
import shutil
#this will accept the directory which needs to be sorted
path=input("enter the name of the directory to be sorted")
#this will create a properly organised list with  the file name
list_of_files = os.listdir(path)
#this will go through each and every file
for file in list_of_files:
    name,ext=os.path.splitext(file)
    #this is going to store extension type
    ext=ext[1:]
    #this will force next iteration if its a directory
    if ext==" ":
        continue
    #this will move the files to the directory where the name ext exist
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    #this will create a new directory if it doesnt exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)