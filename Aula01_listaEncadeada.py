class No:
    def __init__(self, valor, proximo):
        self.__valor = valor
        self.__proximo = proximo

    def __str__(self):
        return f"Nó ({self.__valor}, {self.__proximo}) "

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