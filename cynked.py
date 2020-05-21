#mainSync.py
import subprocess
import os
import glob
import toml
import sys

config_server = toml.loads(open("server.toml", "r").read())
config_home = toml.loads(open("home.toml", "r").read())

try:
    pull = sys.argv[1] == "pull"
    push = sys.argv[1] == "push"
except IndexError:
    print("Error: Please enter the correct number of commands (either push or pull)")
except:
    print("Error: Uh-oh, not sure what happened here. If error persists, please contact the creator.")

overwrite = True

if pull:
    subprocess.call(["ssh", config_server["user"] + "@" + config_server["ip"], "cd " + config_server["ks"] + "&& python3 cynked.py push"])
elif push:
    for file in glob.glob(str(config_home["file"]) + "*.*"):
        print("Writing " + file[file.rindex("/") + 1:])
        subprocess.call(["scp",file,config_server["user"] + "@" + config_server["ip"] + ":" + config_server["file"]])
else:
    print("Error: Please enter a valid command in the command line (either push or pull)")
