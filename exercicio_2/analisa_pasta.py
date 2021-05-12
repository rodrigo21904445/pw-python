import os
import csv

def pede_pasta():
    nome = input("Insira um caminho para a pasta: ")
    return nome

def faz_calculos(path):
    dic_info = {}
    # iterate every file in that directory
    for filename in os.listdir(path):
        dic_key = filename.split(".")[1]
        # if key exists, add info 
        if dic_info.__contains__(dic_key):
            dic_info[dic_key]["volume"] += os.stat(filename).st_size
            dic_info[dic_key]["quantidade"] += 1
        else:
            # if key doesnt exist, creates a dict
            dic_info[dic_key] = {}
            dic_info[dic_key]["volume"] = 1
            dic_info[dic_key]["quantidade"] = os.stat(filename).st_size
    return dic_info

def guarda_resultados(dic_info):
    with open("analisa_pasta.csv", "w", newline="") as file:
        writer = csv.writer(file)
        file.write("extensao, volume, quantidade")
        for key, value in dic_info.items():
            writer.writerow([key, dic_info[key]["volume"], dic_info[key]["quantidade"]])
       # file_syntax = ["extensao", "volume", "quantidade"]
       # writer = csv.DictWriter(file, fieldnames=file_syntax)
       # writer.writeheader()
       # for info in dic_info:
           # key = get_key(dic_info, dic_info[info])
           # writer.writerow(key)
           # writer.writerow(dic_info[info])

if __name__ == "__main__":
    path = pede_pasta()
    calculos = faz_calculos(path)
    guarda_resultados(calculos)
