"""

    Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas 
    e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

"""

numero= int (input('coloque um numero:'))
numero<1000



if numero >= 900:
    print (f'9 centenas') 
elif numero >= 800:
    print (f'8 centenas') 
elif numero >= 700:
    print (f'7 centenas')
elif numero >= 600:
    print (f'6 centenas') 
elif numero >= 500:
    print (f'5 centenas') 
elif numero >= 400:
    print (f'4 centenas') 
elif numero >= 300:
    print (f'3 centenas') 
elif numero >= 200:
    print (f'2 centenas') 
elif numero >= 100: 
    print (f'1 centena')
elif numero >= 0: 
    print (f'0 centenas')




if numero >= 900:
  numero= numero - 900
elif numero >= 800:
    numero= numero - 800
elif numero >= 700:
      numero= numero - 700
elif numero >= 600:
     numero= numero - 600
elif numero >= 500:
      numero= numero - 500
elif numero >= 400:
    numero= numero - 400
elif numero >= 300: 
     numero= numero - 300
elif numero >= 200: 
     numero= numero - 200
elif numero >= 100: 
     numero= numero - 100
elif numero >= 0: 
     numero= numero - 0       


if numero>= 90:
    print ('9 dezenas')
elif numero>= 80:
    print ('8 dezenas')
elif numero>= 70:
    print ('7 dezenas')
elif numero>= 60:
    print ('6 dezenas')
elif numero>= 50:
    print ('5 dezena')
elif numero>= 40:
    print ('4 dezenas')
elif numero>= 30:
    print ('3 dezenas')
elif numero>= 20:
    print ('2 dezenas')
elif numero>= 10:
    print ('1 dezena')
elif numero>= 0:
    print ('0 dezenas')    


if numero >= 90:
  numero= numero - 90
elif numero >= 80:
    numero= numero - 80
elif numero >= 70:
      numero= numero - 70
elif numero >= 60:
     numero= numero - 60
elif numero >= 50:
      numero= numero - 50
elif numero >= 40:
    numero= numero - 40
elif numero >= 30: 
     numero= numero - 30
elif numero >= 20: 
     numero= numero - 20
elif numero >= 10: 
     numero= numero - 10   
elif numero >= 0: 
     numero= numero - 0  




if numero== 9:
    print ('9 unidades')
elif numero== 8:
    print ('8 unidades')
elif numero== 7:
    print ('7 unidades')
elif numero== 6:
    print ('6 unidades')
elif numero== 5:
    print ('5 unidades')
elif numero== 4:
    print ('4 unidades')
elif numero== 3:
    print ('3 unidades')
elif numero== 2:
    print ('2 unidades')
elif numero== 1:
    print ('1 unidade')
elif numero== 0:
    print ('0 unidade')











