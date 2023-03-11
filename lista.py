import csv
class Lista:
    def __init__(self) ->None:
        self.tamanho = 10
        self.vetor = [None]*self.tamanho
        self.qtd = 0
    
    def adicionar(self,aluno):
        if self.qtd < self.tamanho:
            self.vetor = [aluno] + self.vetor
            self.qtd = self.qtd + 1
            return self.vetor
        else:
            self.expandir_vetor()
            self.adicionar(aluno)

    def expandir_vetor(self):
        novo_tamanho = self.tamanho + 1
        vetor_temporario = [None] * novo_tamanho
        for i in range(self.tamanho):
            vetor_temporario[i] = self.vetor[i]
        self.tamanho = novo_tamanho
        self.vetor = vetor_temporario

    def listar(self):
        for i in range(self.qtd):
            print(self.vetor[i])

    def salvar_arquivo():
        with open("alunos.csv", mode='w',newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(['cpf'],['Nome'],['Matricula'])

            for aluno in self.vetor:
                escritor_csv.writerow(aluno)


    
lista = Lista()
lista.adicionar(1)
lista.listar()
lista.salvar_arquivo()



'''
Crie um menu para o programa e insira as seguintes opções:
Criar novos elementos
Salvar em arquivo
Carregar do arquivo
Listar
Buscar pelo id
Remover elemento pelo id
Limpar Arquivo
'''