class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/!")
    
    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
            print(f"{self.marca} reduziu {self.velocidade} km/h.")

    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - "
        f"cor: {self.cor}, velocidade: {self.velocidade} km/h")

moto1 = Moto("Yamaha", "trail XTZ", 2020, "azul")
moto2 = Moto("Honda", "Civic", "2019", "Amarela")

print(moto1.detalhes())
print(moto2.detalhes())

moto1.acelerar(50)
moto2.acelerar(30)

moto1.frear(20)
moto2.frear(15)

print(moto1.detalhes())
print(moto2.detalhes())
