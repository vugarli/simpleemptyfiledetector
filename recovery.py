from ctypes import sizeof
from ctypes.wintypes import PINT
from datetime import date, datetime
from os.path import join
from os import walk

# rootdir =  "C:\\Users\\vuqar\Desktop\\recovery\\"
rootdir = "E:\\100CANON"
logdir = "C:\\Users\\vuqar\\Desktop\\"

files = []

for (dir,dirnames,filenames) in walk(rootdir):
    for file in filenames:
        print(file)
        files.append(join(dir,file))

print("Files discovered: ",len(files))
print("Press any button to continue")
input()

emptyfiles = []
nonemptyfiles = []

for f in files:
    with open(f, 'rb') as file:
        bytes = file.read()
        if sum(bytes) == 0:
            emptyfiles.append(f)
        else:
            nonemptyfiles.append(f)

print("Process finished... ",len(emptyfiles)," empty files discovered")
input()

logfile = (("".join((date.ctime(datetime.now())).split()))+".txt").replace(":","_")

with open((logdir+logfile),"w") as log:
    for f in nonemptyfiles:
        log.write(f+"\n")

print("Type delete to delete all empty files....")
check = input()
if(check != "delete"): exit

