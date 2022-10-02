from ctypes import sizeof
from ctypes.wintypes import PINT
from datetime import date, datetime
from os.path import join
from os import walk

# rootdir =  "C:\\Users\\vuqar\Desktop\\recovery\\"


rootdir = "H:\\pics"
logdir = "C:\\Users\\vuqar\\"

files = []

for (dir,dirnames,filenames) in walk(rootdir):
    for file in filenames:
        print(file)
        files.append(join(dir,file))

filecount = len(files)

print("Files discovered: ",len(files))
print("Press any button to continue")
input()

emptyfiles = []
nonemptyfiles = []
counter=0
for f in files:
    print(filecount-counter, " remaining..")
    counter+=1
    with open(f, 'rb') as file:
        bytes = file.read()
        for b in bytes:
            if b != 0:
                nonemptyfiles.append(f)
                break
        emptyfiles.append(f)
        
            

print("Process finished... ",len(emptyfiles)," empty files discovered & ",len(nonemptyfiles)," discovered")
input()

logfile = (("".join((date.ctime(datetime.now())).split()))+".txt").replace(":","_")

with open((logdir+logfile),"w") as log:
    for f in nonemptyfiles:
        log.write(f+"\n")
    

print("Type delete to delete all empty files....")
check = input()
if(check != "delete"): exit

