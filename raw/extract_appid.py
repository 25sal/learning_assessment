
import glob
import numpy as np

jsessionid = "C1B5BD636F4827895D02512534A7032F"

request = "https://esse3.cressi.unicampania.it/auth/docente/CalendarioEsami/ListaStudentiEsameExcel.xls;jsessionid="+jsessionid+".jvm2b?AA_ID=2015&MIN_AA_CAL_ID=0&CDS_ID=10364&AD_ID=16678&APP_ID=_REPLACEME_&SORT_ORDER=ascending&SORT_CODE=2&gruppo_giud_cod=VOTO_1&AA_CAL_ID=2015&FMT_COGN_NOME=CN&VIEW_DETT_ESACOM=1&VIS_DETT=-100&TV_GRUPPO_VOTO_APP_ID=1&TV_GRUPPO_GIUD_COD=&default_ins_esiti=1&excel=1%0A"




def extract_APPID():
    with open("appelli3.html", "r") as fp:
        lines = fp.readlines()
        for line in lines:
            temp = line.split("&")
            #print(temp[8][9:-2]+ " *")
            
            updated_request = request.replace("_REPLACEME_", temp[3][7:])
            print(updated_request)
            

def process_csv_files():
    csv_files = glob.glob("./data/results/*.utf8")   
    for csv_file in csv_files:
        #print(csv_file)
        with open(csv_file, "r") as template:
            lines = template.readlines()
            
            found_matr = False
            for i in range(10,len(lines)):
                if "Date Appello" in lines[i]:
                    tokens = lines[i].split(",")
                    exam_date = tokens[3][0:10]
                    # print(exam_date)
                
                if found_matr:
                    tokens = lines[i].split(",")
                    if len(tokens) > 8:

                        print(tokens[2]+","+tokens[8]+","+exam_date[-4:]+exam_date[3:5]+exam_date[0:2])
                if "Matricola" in lines[i]:
                    found_matr = True
                

                
            

if __name__ == "__main__":
    process_csv_files()
    # extract_APPID()

