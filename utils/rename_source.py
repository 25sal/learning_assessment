import glob
import shutil
import os

sessions = glob.glob("/home/salvatore/eclipse-workspace/elpro/data/anonymized/20*")
for session in sessions:
    userdirs = glob.glob(session + "/users/A13*")
    for userdir in userdirs:
        projects = glob.glob(userdir + "/*")
        for project in projects:
            source_files = glob.glob(project + "/*.c")
            for filename in source_files:
                if os.path.getsize(filename) == 0:
                    os.remove(filename)
                else:
                    shutil.move(filename, os.path.dirname(filename) + "/main.c")
