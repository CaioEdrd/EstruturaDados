def quickSort(lista):
        
        if len(lista) <= 1 :
            return lista  
        else :
            central = len(lista)//2 
            pivo = lista[central]
        
        
        esquerda = [x for x in lista if x < pivo]
        meio =  [x for x in lista if x == pivo]
        direita = [x for x in lista if x > pivo]

        return quickSort(esquerda) + meio + quickSort(direita)

listaDesordenada = [1,5,7,9,2,15,4,18,22,33,6] # -> Pivo 15 -> 1,2,4,5,6,7,9,15,18,22,33 
print(quickSort(listaDesordenada))

listaDesordenada2 = [1,7,6,5,8,3,4,122,15,14,199]
print(quickSort(listaDesordenada2))