def operation(lista):
    results = list()
    for n in range(len(lista)):
        if lista[n]%1.25 == 0:
            results.append(lista[n])
    if len(lista) > 0:
        return results
    else:
        return 'no matches'
    
a_sequence = (25, 35,40,125,50,313.5)
print(operation(a_sequence))