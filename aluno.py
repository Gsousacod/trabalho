#Cadastro de aluno;

class Aluno:
    def __init__(self,cpf,nome,matricula) -> None:
        self.cpf = cpf
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'CPF: {self.cpf}\nNome: {self.nome}\nMatricula:{self.matricula}'

