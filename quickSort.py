def quickSort(lista):
        
        if len(lista) == 1 :
            return lista  
        elif len(lista) > 0:
            central = len(lista)//2 
            pivo = lista[central]
        else:
            return []
        
        esquerda = [x for x in lista if x < pivo]
        meio =  [pivo]
        direita = [x for x in lista if x > pivo]

        return quickSort(esquerda) + meio + quickSort(direita)

listaDesordenada = [1,5,7,9,2,15,4] #1,2,4,5,7,9,15 -> Pivo 5
print(quickSort(listaDesordenada))

listaDesordenada2 = [1,7,6,5,8,3,4,122,15,14,199]
print(quickSort(listaDesordenada2))