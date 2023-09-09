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

    def maior_valor(self):
        if self.raiz == None:
            return 0
        else:
            return self.maior_valor_recursivo(self.raiz)
        
    def maior_valor_recursivo(self, no):
        if no is None:
            return None
        maior_valor = no.valor
        if no.esquerda is not None:
            valor_esquerda = self.maior_valor_recursivo(no.esquerda)
            if valor_esquerda > maior_valor:          
                maior_valor = valor_esquerda
        if no.direita is not None:
            valor_direita = self.maior_valor_recursivo(no.direita)
            if valor_direita > maior_valor:
                maior_valor = valor_direita
        return maior_valor 

def maior_valor_arvore():

    a = ArvoreBinaria()

    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    
    print()
    print('Maior valor na árvore:', a.maior_valor())

maior_valor_arvore()