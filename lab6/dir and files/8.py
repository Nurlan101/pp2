import os

path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files\Delete"

if os.path.exists(path) and os.access(path, os.X_OK):
    path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files\Delete"
    os.chdir(path)
    file_to_delete = "Something"
    os.remove(file_to_delete)
else:
    print('Path not found or is not accessible')
