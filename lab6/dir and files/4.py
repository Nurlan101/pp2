import os

path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files"
os.chdir(path)

F_name = "Num of Lines.txt"
with open(F_name) as f:
    count = 0
    for lines in f:
        count += 1
    
    print(count)
    f.close()