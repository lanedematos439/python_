class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome
        self.nome = input("qual o seu nome? ")

    def falar(self, mensagem=None):
        self.mensagem = input("O que você quer dizer? ")
       
    def cantar(self, musica=None):
        self.musica = input("Qual música você quer cantar? ")
       
    def estudar(self, materia=None):
        self.materia = input("o que voce está estudando? ")
        
    def eu(self):
        return f'Meu nome é {self.nome}, e eu gostaria de falar {self.mensagem}, eu gosto de cantar a musica {self.musica}, e estou estudando {self.materia}.'

p = Pessoa()
p.falar()
p.cantar()
p.estudar()
print(p.eu())