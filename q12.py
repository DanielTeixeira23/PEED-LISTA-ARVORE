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

    def procurar_nos(self, valor):
        if self.raiz is None:
            return False
        else:
            return self.procurar_nos_na_arvore(self.raiz, valor)
    
    def procurar_nos_na_arvore(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if self.procurar_nos_na_arvore(no.esquerda, valor):
            return True
        if self.procurar_nos_na_arvore(no.direita, valor):
            return True
            
    def remover_nos(self, v):
        if self.raiz is None:
            return None
        else:
            return self.remover_nos_recursivo(self.raiz, v)
    
    def remover_nos_recursivo(self, no, v):
        if no is None:
            return None
        if v < no.valor:
            no.esquerda = self.remover_nos_recursivo(no.esquerda, v)
        elif v > no.valor:
            no.direita = self.remover_nos_recursivo(no.direita, v)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            
            menor_valor_direita = self.menor_valor(no.direita)
            no.valor = menor_valor_direita
            no.direita = self.remover_nos_recursivo(no.direita, menor_valor_direita)
        return no

    def menor_valor(self, no):
        if no.esquerda is None:
            return no.valor
        else:
            return self.menor_valor(no.esquerda)
        
def verificar_remover_no():
    
    a = ArvoreBinaria()

    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    print()
    
    num_verificar = int(input('Informe um número para verificar se ele está presente na árvore: '))
    if a.procurar_nos(num_verificar):
        print(f'O número {num_verificar} está presente na árvore.')
        a.remover_nos(num_verificar)
        print('Nó removido com sucesso.')
        print()
        print('Nós presentes na árvore após remoção:')
        a.mostrar_pre_ordem()
    else:
        print('Número não está presente na árvore!')
    
verificar_remover_no()