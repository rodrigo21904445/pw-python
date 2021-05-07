import os
import json

def pede_nome():
    while 1:
        path = os.getcwd()
        nome = input("Qual é o nome do ficheiro? ")
        #print(path + "\\" + "analisa_ficheiro" + "\\" + nome)
        if os.path.isfile(path + "\\" + "analisa_ficheiro" + "\\" + nome):
            return nome

def gera_nome():
    nome = input("Qual é o nome do ficheiro? ")
    with open(nome, "r") as src_file, open(nome.split(".")[0] + ".json", "w") as dest_file:
        src_text = src_file.read()
        dest_file.write(src_text)


if __name__ == "__main__":
    #pede_nome()
    #print(pede_nome())
    gera_nome()