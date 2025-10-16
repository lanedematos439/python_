class Casa:
    def __init__(self, cor=None, quartos=None, banheiros=None, tamanho=None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.cor = input("Qual a cor da casa? ")
        self.quartos = input("Quantos quartos a casa tem? ")
        self.banheiros = input("Quantos banheiros tem a casa? ")
        self.tamanho = input("Qual o tamanho da casa em m²? ")

        return f"Esta casa é {self.cor}, tem {self.quartos} quartos, {self.banheiros} banheiros e {self.tamanho}m²."
    
cs = Casa()
print(cs.descrever())