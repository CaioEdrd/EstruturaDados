class Fila:
    def __init__(self):
        self.__lst = []
    
    def __str__(self):
        return str(self.__lst)
    
    def _ordenar(self):
        if self.vazio(): return None
        self.__lst.sort(key=lambda x: x[1])

    def vazio(self):
        return len(self.__lst) == 0

    def adicionar(self,valor,prioridade):
        self.__lst.append((valor,prioridade))
        self._ordenar()

    def remover(self):
        if self.vazio(): return None
        r = self.__lst[0]
        self.__lst.remove(r)
        return r

    def olhar(self):
        if self.vazio(): return None

        return self.__lst[0]
    
f1 = Fila()
f1.adicionar('b',1)
f1.adicionar('c',3)
f1.adicionar('a',2)

print(f1)
# print(f'Elemento removido: {f1.remover()}')

# print(f'Próximo elemento: {f1.olhar()}')
# print(f1)