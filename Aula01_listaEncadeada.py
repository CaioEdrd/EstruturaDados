class No:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

    def __str__(self):
        return f"Nó ({self.valor}, {self.proximo}) "

class ListaEnc:
    def __init__(self):
        self.__topo = None
        self.__final = None

    def __str__(self):
        if self.__topo:
            return str(self.tam())
        else:
            return "Vazio"

    def vazio(self): #Verificação da lista, se está vazia
        return self.__topo == None

    def adicao(self, val):
        n = No(val, None) #adição do Nó
        if self.vazio():
            self.__topo = n #Se a lista estiver vazia, adiciona o nó no inicio
        else:
            self.__final.proximo = n
        self.__final = n

    def tam(self):
        if self.vazio(): return 0

        p = self.__topo
        c= 0 
        while p != None:
            c+=1
            p = p.proximo
        return c

    def listarElementos(self):
        if self.vazio(): return "Vazio"

        while True:
            print(self.__topo)


l1 = ListaEnc()
l1.adicao(1)
l1.adicao(10)
print(l1)
print(l1.tam())

'''
#Forma manual de implementação na lista
nb = No("B", None)  #Inserção no final
ni = No("I", nb)
nh = No("H", ni)
ng = No("G", nh)
nf = No("F", ng)
nz = No("Z", nf) #Inserção nessa posição
nc = No("C", nz)
na = No("A", nc)

print(ni)

l1 = na
print(l1)
'''