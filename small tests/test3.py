lisa = ['pippo','baudo','ciccio','cannolo']
print(type(' '.join(lisa)))

listanew = sorted(lisa)

x = lisa.sort()
print(listanew)
print(x)
b = lisa.copy()
print(b)



dizionario = {'gigi':33,
              'gogo':44,
              'toni':19,
              'ema':21}
print(dizionario)
dizionario.keys().sort()
print(dizionario)




lisa = ['pippo','baudo','ciccio','cannolo']
print(lisa)
lisa.sort(reverse=True)
print(lisa)
lisa.sort()
print(lisa)


