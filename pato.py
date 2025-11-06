class Pato:
    def quack(self):
        print("o pato faz Quack!")

class Pessoa:
    def quack(self):
        print("A pessoa imita um pato: Quack!")

    def comer(self):
        print("A pessoa está comendo.")

def fazer_quack(obj):
    obj.quack()

p = Pato()
h = Pessoa()

class Gravacao:
    def quack(self):
        print("Som gravado: Quack quack!")

class Robo:
    def quack(self):
        print("Robo: Q-U-A-C-K em som metálico!")

objetos = [Pato(), Pessoa(), Gravacao(), Robo()]

for obj in objetos:
    obj.quack()