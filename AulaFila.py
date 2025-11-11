class Fila:
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
        r = self.__lst[0]
        self.__lst.remove(r)
        return r

    def olhar(self):
        if self.vazio(): return None

        return self.__lst[0]

        
f1 = Fila()
f1.adicionar('a')
f1.adicionar('b')
f1.adicionar('c')
f1.adicionar('d')
print(f1)
print(f'Elemento removido: {f1.remover()}')

print(f'Próximo elemento: {f1.olhar()}')
print(f1)