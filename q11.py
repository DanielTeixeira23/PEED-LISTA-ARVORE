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
    
    def mostrar_in_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_in_ordem_recursivo(self.raiz)

    def mostrar_in_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_in_ordem_recursivo(no.esquerda)
        print(no.valor, end=' ')
        if no.direita is not None:
            self.mostrar_in_ordem_recursivo(no.direita)
      
    def mostrar_em_nivel(self):
        if self.raiz is None:
            return
        else:
            print(self.raiz.valor, end=' ')
            self.mostrar_em_nivel_recursivo(self.raiz)

    def mostrar_em_nivel_recursivo(self, no):
        if no.esquerda is not None:
            print(no.esquerda.valor, end=' ')
        if no.direita is not None:
            print(no.direita.valor, end=' ')

        if no.esquerda is not None:
            self.mostrar_em_nivel_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_em_nivel_recursivo(no.direita)
    
    def arvore_de_busca_valida(self):
        if self.raiz is not None:
            if self.raiz.esquerda is None and self.raiz.direita is None:
                return True
            else: 
                valor_min = float('-inf')
                valor_max = float('inf') 
                return self.verificar_arvore_de_busca_valida(self.raiz, valor_min, valor_max)
        return False
    
    def verificar_arvore_de_busca_valida(self, no, valor_min, valor_max):
        if no is None:
            return True
        if valor_min < no.valor < valor_max:
            return (self.verificar_arvore_de_busca_valida(no.esquerda, valor_min, no.valor) 
                    and self.verificar_arvore_de_busca_valida(no.direita, no.valor, valor_max))
        else:
            return False
        
def verificar_arvore():

    a = ArvoreBinaria()

    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    print('Valores em nível: ')
    a.mostrar_em_nivel()
    print()
    print('Valores em in-ordem: ')
    a.mostrar_in_ordem()
    print()
        
    if a.arvore_de_busca_valida():
        print("A árvore é uma árvore de busca válida.")
    else:
        print("A árvore não é uma árvore de busca válida.")
        
verificar_arvore()