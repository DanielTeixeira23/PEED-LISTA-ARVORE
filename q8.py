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
        
def exibir_em_nivel():            
    arvore = ArvoreBinaria()
    
    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º número: '))
        arvore.inserir_em_nivel(num)
        
    print()  
    print('Números em nível:')
    arvore.mostrar_em_nivel()
    
exibir_em_nivel()