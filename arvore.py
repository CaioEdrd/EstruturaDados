class No:
    def __init__(self,valor):
        self.__V = valor
        self.Lsub = []
    
    def __str__(self):
        lsn =[f"{str(sn)}" for sn in self.Lsub]
        return f"Valor:{self.__V}, SubNos: {lsn}"
    
r=No(5)
r.Lsub.append(No(10))
r.Lsub.append(No(7))

n=No(3)
c = No(5)

n.Lsub.append(c)
n.Lsub.append(No(6))


r.Lsub.append(n)

print(r)

#fazer metodo construtor que aceite passar uma lsita de nós e ser adicionado na arvore