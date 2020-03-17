
s = input('Ingresa la palabra: ')

def countPalindromes(s):
    s = str(s).lower()
    lista = []

    if (s == s[::-1]):
        lista.append(s)
        #print(lista)    
        for i in range(1, len(s)):
            for j in range(0, len(s) - i + 1):
                ss = s[j:i + j]
                print(ss)
                if ss == ss[::-1]:
                    lista.append(ss)
    print(len(lista))
    
    print(lista)
                

    
 
            
        

countPalindromes(s)