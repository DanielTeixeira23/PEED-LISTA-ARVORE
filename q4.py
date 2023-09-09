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

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_raiz(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            print('Raiz:', self.raiz.valor, end=' ')   

    def altura_da_arvore(self):
        if self.raiz is None:
            return 0
        else:
            return self.altura_arvore(self.raiz) - 1

    def altura_arvore(self, no):
        if no is None:
            return 0
        else:
            return max(self.altura_arvore(no.esquerda), self.altura_arvore(no.direita)) + 1
        
def altura_arvore():

    a = ArvoreBinaria()

    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print()
    print('Valores inseridos com sucesso.')
    print('Altura da árvore:', a.altura_da_arvore())

altura_arvore()