dinheiro = True
senha = True

if dinheiro == True and senha == True:
    print ('sacar')

elif dinheiro == True and senha == False:
    print('senha incorreta')

elif dinheiro == False and senha == True:  
    print('saldo insuficiente')

elif dinheiro == False and senha == False:
    print('saldo e senha invalidos')
