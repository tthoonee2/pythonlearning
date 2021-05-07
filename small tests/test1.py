lista = [
    '4',
    'python',
    'z'
]
n = 0 
listautf = []
while n<len(lista):
    listautf.append(lista[n].encode('utf-8'))
    listautf[n] = listautf[n].hex()
    print(listautf[n])
    n += 1
    
    
    
