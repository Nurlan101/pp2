import os
import string

path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files"
os.chdir(path)

if not os.path.exists("Letters"):
   os.makedirs("Letters")

path = r"C:\Users\User\Documents\GitHub\pp2\lab6\dir and files\Letters"
os.chdir(path)

for l in string.ascii_uppercase:
   with open(l + ".txt", "w") as f:
       f.close()