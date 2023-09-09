class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita) 

    def verificar_nos(self, valor):
        if self.raiz is None:
            return False
        else:
            return self.verificar_nos_na_arvore(self.raiz, valor)
    
    def verificar_nos_na_arvore(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if self.verificar_nos_na_arvore(no.esquerda, valor):
            return True
        if self.verificar_nos_na_arvore(no.direita, valor):
            return True
        
def verificacao():

    a = ArvoreBinaria()

    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')

    verificar_num = int(input('Informe um número para verificar se ele está presente na árvore: '))
    if a.verificar_nos(verificar_num):
        print('Número presente na árvore')
    else:
        print('Número não está presente na árvore!')

verificacao()