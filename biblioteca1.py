class Livro():
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def apresentar(self):
        return f"O titulo do livro é {self.titulo}, o autor deste livro é {self.autor} e o ano que foi lançado foi {self.ano_publicacao}."
    
class LivroDidatico(Livro):
    def __init__(self, titulo=None, autor=None, ano_publicacao=None, disciplina=None):
        if titulo is None: 
            titulo = input("Digite o titulo do Livro Didatico: ")
        if autor is None:
            autor = input("Digite o nome do autor(a) deste livro: ")
        if ano_publicacao is None:
            ano_publicacao = input("Digite o ano de publicação deste livro didático: ")
        if disciplina is None:
            disciplina = input("Digite de qual disciplina é esta obra: ")
        
        super().__init__(titulo, autor, ano_publicacao)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        return f"O título do livro é {self.titulo}, seu autor(a) é {self.autor}, o ano que lançou foi {self.ano_publicacao} e ele pertence à disciplina {self.disciplina}."

class LivroFiccao(Livro):
    def __init__(self, titulo=None, autor=None, ano_publicacao=None, genero=None):
        if titulo is None:
            titulo = input("Digite o título do seu livro: ")
        if autor is None:
            autor = input("Digite o nome do autor(a): ")
        if ano_publicacao is None:
            ano_publicacao = input("Digite o ano de publicação: ")
        if genero is None:
            genero = input("Digite o gênero do seu livro: ")

        super().__init__(titulo, autor, ano_publicacao)
        self.genero = genero
        
    def apresentar(self) -> str:
        return f"O título do livro é {self.titulo}, seu autor(a) é {self.autor}, o ano que lançou foi {self.ano_publicacao} e ele é do gênero {self.genero}."


def main():
    l1 = Livro("Cinco Minutos", "José de Alencar", "1856")
    print(l1.apresentar())

    l2 = LivroDidatico()
    print(l2.apresentar())

    l3 = LivroFiccao()
    print(l3.apresentar())
  

if __name__ == "__main__":
    main()  
       