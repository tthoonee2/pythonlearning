def xo(s):
     xs = 0
     os = 0
     val = False
     s = s.lower()
     for letter in s:
        if letter == 's':
            xs += 1
        elif letter == 'o':
            os += 1
        
     print(xs,os)        
     if xs == os:
        val = True
     elif xs== 0 and xo == 0:
        val == True
    
     return val