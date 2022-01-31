import os
import shutil
dir= "/home/salvatore/eclipse-workspace/elpro/data/clang_test"


infile = open(dir+"/files.txt", "r")
sources = infile.readlines()
for line in sources:
    tokens = line.split("/")
    print(tokens[1], tokens[3])
    if not os.path.isdir("data/"+tokens[1]+"/users/compile"):
        os.makedirs("data/"+tokens[1]+"/users/compile")

    print('gcc -c ' + dir+"/"+line[:-1] + " > temp.cc")
    stream = os.system('clang -c ' + dir+"/"+line[:-1] + " 2> temp.cc" )
    f = open("temp.cc", "r")
    txt = f.read()
    if "error" in txt:
       print("error_"+tokens[3]+"_000000")
       shutil.copy("temp.cc", "data/"+tokens[1]+"/users/compile/"+"error_"+tokens[3]+"_000000")
    else:
       print("ok_" + tokens[3]+"_000000")
       shutil.copy("temp.cc", "data/" + tokens[1] + "/users/compile/" + "ok_" + tokens[3] + "_000000")

    f.close()
os.system("rm *.o")
