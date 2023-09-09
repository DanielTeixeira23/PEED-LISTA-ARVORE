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
    
    def percurso_raiz_ao_no(self, valor):
        percurso = self.percurso_raiz_ao_no_recursivo(self.raiz, valor)
        if percurso:
            print(f'Caminho até o nó {valor}:', end=' ')
            for valor in percurso:
                print(valor, end=' ')
            print()
        else:
            print(f'O nó {valor} não está presente na árvore!')

    def percurso_raiz_ao_no_recursivo(self, no, valor):
        if no is None:
            return None
        
        if no.valor == valor:
            return [no.valor]
        caminho_a_esquerda = self.percurso_raiz_ao_no_recursivo(no.esquerda, valor)
        
        if caminho_a_esquerda:
            return [no.valor] + caminho_a_esquerda
        caminho_a_direita = self.percurso_raiz_ao_no_recursivo(no.direita, valor)
        
        if caminho_a_direita:
            return [no.valor] + caminho_a_direita
        return None

def percurso_em_arvore():
    
    a = ArvoreBinaria()

    qnt_valores = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt_valores):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    print()
    
    x = int(input('Informe um nó e veja o percurso até chegar nele: '))
    a.percurso_raiz_ao_no(x)
    
percurso_em_arvore()