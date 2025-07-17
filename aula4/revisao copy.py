#modulo                                             = atribuiçao
#print(12 % 4 == 0)#0 É O RESTO da divisao          ==comparaçao
n= int (input('digite um valor numerico:'))
if (n %2 ==0):                                     #!=Diferenciaçao
    print(f'o {n} digitado é par')
elif (n % 2 == 1):
    print(f'o {n} digitado é impar')
else:
    print('o numero digitado é invalido')