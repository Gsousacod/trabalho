import random 
from faker import Faker
from aluno import Aluno
from lista import Lista

fake = Faker()
lista = Lista()

def menu():
    respo = input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n----------------Escolha uma opção:----------------- \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n1 - Criar novos elementos \n2 - Salvar em arquivo\n3 - Carregar do arquivo\n4 - Lista\n5 - Buscar pelo id\n6 - Remover elemento pelo id\n7 - Limpar Arquivo\n0 - Sair")
    return respo
def criar_elemento():
    quantidade = int(input('Quantos alunos deseja matricular?'))
    question = input("Deseja criar as matriculas de forma ateatoria? s/n")
    question2 = question.lower()
    for i in range(quantidade):
        if question2:
            matricula = random.randint(1,1000)
        else:
            matricula = i +1
        aluno = Aluno(random.randint(1000,2000),Faker().name(), matricula)
        lista.adicionar(aluno)
    print("Elementos criados com sucesso!!")





resp = menu()
while True:
    if resp == '1':
        criar_elemento()
    elif resp == '2':
        pass
    elif resp =='3':
        pass
    elif resp == '4':
        lista.listar()
    elif resp == '5':
        pass
    elif resp == '6':
        pass
    elif resp == '7':
        pass
    elif resp == '0':
        break
    resp = menu()