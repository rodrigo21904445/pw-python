import os
import csv
from matplotlib import pyplot as plt

def pede_pasta():
    nome = input("Insira um caminho para a pasta: ")
    return nome

def faz_calculos(path):
    dic_info = {}
    # iterate every file in that directory
    for filename in os.listdir(path):
        # if filename is a folder continues
        if filename is not os.path.isfile(path):
            continue
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
        file.write("extensao, volume, quantidade\n")
        for key, value in dic_info.items():
            writer.writerow([key, dic_info[key]["volume"], dic_info[key]["quantidade"]])

def faz_grafico_queijos(title, key_list, values_volume_list, values_quantidade_list):
    plt.pie(key_list, labels=values_volume_list, autopct="%1.0f%%")
    plt.pie(key_list, labels=values_quantidade_list, autopct="%1.0f%%")
    plt.title(title)
    plt.show

def faz_grafico_barras(title, key_list, values_volume_list, values_quantidade_list):
    plt.bar(key_list, values_volume_list)
    plt.bar(key_list, values_quantidade_list)
    plt.title(title)
    plt.show
