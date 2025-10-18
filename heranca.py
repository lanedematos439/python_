class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}"
    
class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.matricula = matricula
    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matricula {self.matricula}"
    
class Professor(Pessoa):
    def __init__(self, nome: str, disciplina: str) -> None:
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        return f"Professor {self.nome} de {self.disciplina}"
        
class BolsaMixin:
    def calcular_bolsa(self) -> float:
        return 1200.00
    
class AlunoBolsista(BolsaMixin, Aluno):
    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e recebo bolsa de R$ {self.calcular_bolsa():2f}"
    
    def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
        return [p.apresentar() for p in pessoas]
    
    def main() -> None:
        p = Pessoa("João")
        a = Aluno("Ana", "A123")
        pr = Professor("Carlos", "Matemática")
        ab = AlunoBolsista("Beatriz", "B456")

        resultados = apresentar_todos([p, a, pr, ab])
        for r in resultados:
            print(r)

        print("",
              f"isintance(ab, Pessoa): {isinstance(ab, Pessoa)}",
              f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}",
              f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}",
              sep="\n")
        print("MRO AlunoBolsista: ")
        for cls in AlunoBolsista.__mro__:
            print(" -", cls.__name__)

    if __name__ == "__main__":
        main()
    
        


