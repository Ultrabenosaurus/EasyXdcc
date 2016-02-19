import os, pprint, platform;

def check_dirs(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

comp = platform.system()
user = "ghost"

print comp

try:
    cmd = os.popen("whoami")
    try:
        user = cmd.readlines()
        user = user[0].strip("\n")
        if 'Windows' == comp:
            user = user.split("\\")[1]
    finally:
        cmd.close()
except IOError:
    print "Error: can't use CMD"
print user

if 'Windows' == comp:
    sav_dir = "C:/Users/"+user+"/.config/EasyXdcc/"
else:
    sav_dir = "/home/"+user+"/.config/EasyXdcc/"
check_dirs(sav_dir)
sav_file = sav_dir + "queue"

try:
    file = open(sav_file,'rb')
    try:
        for line in file.readlines():
            print line
    finally:
        file.close()
except IOError:
    print "Error: can\'t find file or read data"
