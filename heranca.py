class Pessoa:
    def __init__(self, nome: str, cpf: str, matricula: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome} e meu CPF é {self.cpf}."


class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str, cpf: str) -> None:
        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome} meu cpf é {self.cpf} e minha matrícula é {self.matricula}."


class Professor(Pessoa):
    def __init__(self, nome: None, matricula: None, disciplina: None):
        if nome is None:
            nome = input("Olá, digite o seu nome professor: ")
        if matricula is None:
            matricula = input("Digite o número da matricula do professor: ")
        if disciplina is None:
            disciplina = input("Digite a disciplina que o professor leciona: ")
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self):
        base = super().apresentar()
        return f"Meu nome é {self.nome}, minha matricula é {self.matricula} e sou professor da disciplina de {self.disciplina}"
    
class BolsaMixin:
    def calcular_bolsa(self) -> float:
        return 1200.0 


class AlunoBolsista(BolsaMixin, Aluno):
    def __init__(self, nome: str, matricula: str, cpf: str) -> None:
        super().__init__(nome, matricula, cpf)

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e recebo bolsa de R${self.calcular_bolsa():.2f}."


def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
    return [pessoa.apresentar() for pessoa in pessoas]


def main() -> None:
    p = Pessoa("João", "000.000.000-00")
    a = Aluno("Ana", "A123", "111.111.111-11")
    prof = Professor()
    ab = AlunoBolsista("Beatriz", "B456", "333.333.333-33")

    resultados = apresentar_todos([p, a, prof, ab])
    for r in resultados:
        print(r)

    print("",
          f"isinstance(ab, Pessoa): {isinstance(ab, Pessoa)}",
          f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}",
          f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}",
          sep="\n")

    print("MRO AlunoBolsista:")
    for cls in AlunoBolsista.__mro__:
        print(" -", cls.__name__)


if __name__ == "__main__":
    main()
