import os

path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files"
os.chdir(path)

file_name = "New List.txt"
items = ['User', 'Documents', 'GitHub'] 
with open(file_name, 'w') as f:
    for i in items:
        f.write(i + "\n")
    f.close()