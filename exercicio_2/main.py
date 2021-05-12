import analisa_pasta as analisa

def main():
    path = analisa.pede_pasta()
    calculos = analisa.faz_calculos(path)
    analisa.guarda_resultados(calculos)

    title = "Analisa Pasta"
    key_list = get_keys(calculos)
    values_volume_list = get_values_volume(calculos)
    values_quantidade_list = get_values_quantidade(calculos)
    analisa.faz_grafico_queijos(title, key_list, values_volume_list, values_quantidade_list)
    analisa.faz_grafico_barras(title, key_list, values_volume_list, values_quantidade_list)

def get_keys(dic):
    key_list = []
    for key in dic.items():
        key_list.append(key)
    return key_list

def get_values_volume(dic):
    values_volume_list = []
    for key, value in dic.items():
       values_volume_list.append(dic[key]["volume"])
    return values_volume_list

def get_values_quantidade(dic):
    values_quantidade_list = []
    for key, value in dic.items():
       values_quantidade_list.append(dic[key]["quantidade"])
    return values_quantidade_list

if __name__ == "__main__":
    main()
