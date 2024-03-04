import os

path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files"
os.chdir(path)

copy_from = "z_From.txt"
copy_to = "z_To.txt"
with open(copy_from, 'r') as f:
    with open(copy_to, 'w') as t:
        for line in f:
            t.write(line)
        t.close()
    f.close()