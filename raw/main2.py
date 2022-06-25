import glob
import shutil
import os





lang = "c"
sessions = glob.glob("data/postcovid/2*")
print(sessions)
for session in sessions:
    session_date = os.path.basename(session)
    userdirs = glob.glob(session + "/users/a13*")
    for userdir in userdirs:
        user_id = os.path.basename(userdir)
        projects = glob.glob(userdir + "/"+lang+"/*")
        for project in projects:
            project_type = os.path.basename(project)
            source_file = project + "/main.c"

            if not os.path.isdir(session + "/users/compile"):
                os.makedirs(session + "/users/compile")

            print('gcc -c ' + source_file + " > temp.cc")
            stream = os.system('gcc -c ' + source_file + " 2> temp.cc" )
            f = open("temp.cc", "r")
            try:
                txt = f.read()
                if "error" in txt:
                   print("error_"+user_id+"_000000")
                   shutil.copy("temp.cc", session+"/users/compile/"+"error_"+user_id+"_000000")
                else:
                   print("ok_" + user_id+"_000000")
                   shutil.copy("temp.cc", session + "/users/compile/" + "ok_" + user_id + "_000000")

                f.close()
            except:
                print("error_"+user_id+"_000000")
                shutil.copy("temp.cc", session+"/users/compile/"+"error_"+user_id+"_000000")
                f.close()
    os.system("rm *.o")