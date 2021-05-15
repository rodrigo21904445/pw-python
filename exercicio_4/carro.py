class Automovel():
    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return (self.quant_comb * 100) / self.consumo
    
    def abastece(self, n_litros):
        final_comb = self.quant_comb + n_litros
        if final_comb > self.cap_dep:
            print("Erro: Abasteceu mais do que é possível.")
            return -1
        self.quant_comb = final_comb
        return self.autonomia()

    def percorre(self, n_km):
        autonomia = self.autonomia()
        if autonomia < n_km:
            print("Erro: O automóvel não tem autonomia suficiente para percorrer {km} km.", n_km)
            return -1
        autonomia -= n_km
        return autonomia
            

def main():
    automovel = Automovel(100, 50, 25)
    while 1:
        print("***Opcões***")
        print("1. Quanto combustivel tem? ")
        print("2. Quanto autonomia tem? ")
        print("3. Quantos litros pretende abastecer? ")
        print("4. Quantos km pretende percorrer? ")
        print("5. Sair")
        print("************")
        opc = int(input())

        if(opc == 5):
            return
        
        elif(opc == 1):
            print(automovel.combustivel())
        
        elif(opc == 2):
            print(automovel.autonomia())
        
        elif(opc == 3):
            n_litros = int(input())
            print(automovel.abastece(n_litros))
        
        elif(opc == 4):
            n_km = int(input())
            print(automovel.percorre(n_km))        

if __name__ == "__main__":
    main()