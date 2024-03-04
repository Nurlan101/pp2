import os

path = r"C:\Users\User\Documents\GitHub\pp2"

if os.path.exists(path):
    file = os.path.basename(path)
    dir = os.path.dirname(path)
    print('Filename: ' + file) 
    print('Directory: ' + dir)
    print()
else:
    print('Not found')