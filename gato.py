class Gato:
    def Miau(self):
        print("O gato faz Miau!")

class Pessoa:
    def Miau(self):
        print("A pessoa imita um gato: Miau!")

    def cantar(self):
        print("A pessoa está cantando.")

    def fazer_miau(obj):
        obj.miau()

p = Gato()
h = Pessoa()

class Gravacao:
    def Miau(self):
        print("som gravado: Quack quack!")
    
class Robo:
    def Miau(self):
        print("Robo: M-I-A-U em som metálico!")

objetos = [Gato(), Pessoa(), Robo(), Gravacao()]

for obj in objetos:
    obj.Miau()