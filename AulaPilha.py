class Pilha:
    def __init__(self):
        self.__lst = []
    
    def __str__(self):
        return str(self.__lst)
    
    def vazio(self):
        return len(self.__lst) == 0

    def adicionar(self,valor):
        self.__lst.append(valor)

    def remover(self):
        if self.vazio(): return None
        r = self.__lst[-1]
        self.__lst.remove(r)
        return r

    def olhar(self):
        if self.vazio(): return None

        return self.__lst[-1]

        
p1 = Pilha()
p1.adicionar('a')
p1.adicionar('b')
p1.adicionar('c')
p1.adicionar('d')
print(p1)
print(f'Elemento removido: {p1.remover()}')

print(f'Próximo elemento: {p1.olhar()}')
print(p1)