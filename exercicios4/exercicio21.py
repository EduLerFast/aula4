"""
    Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
    As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
      O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""




numero= int (input('coloque um numero:'))
numero<600




if numero >= 600:
    print (f'6 notas de 100') 
elif numero >= 500:
    print (f'5 notas de 100') 
elif numero >= 400:
    print (f'4 notas de 100') 
elif numero >= 300:
    print (f'3 notas de 100') 
elif numero >= 200:
    print (f'2 notas de 100') 
elif numero >= 100: 
    print (f'1 notas de 100')
elif numero >= 0: 
    print (f'0 notas de 100')




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
    print ('1 nota de 50')
elif numero>= 80:
    print ('1 nota de 50')
elif numero>= 70:
    print ('1 nota de 50')
elif numero>= 60:
    print ('1 nota de 50')
elif numero>= 50:
    print ('1 nota de 50')
elif numero>= 40:
    print ('0 notas de 50')
elif numero>= 30:
    print ('0 notas de 50')
elif numero>= 20:
    print ('0 notas de 50')
elif numero>= 10:
    print ('0 notas de 50')
elif numero>= 0:
    print ('0 notas de 50')    



if numero>= 90:
    print ('4 notas de 10')
elif numero>= 80:
    print ('3 notas de 10')
elif numero>= 70:
    print ('2 notas de 10')
elif numero>= 60:
    print ('1 notas de 10')
elif numero>= 50:
    print ('0 notas de 10')
elif numero>= 40:
    print ('4 notas de 10')
elif numero>= 30:
    print ('3 notas de 10')
elif numero>= 20:
    print ('2 notas de 10')
elif numero>= 10:
    print ('1 nota de 10')
elif numero>= 0:
    print ('0 notas de 10')


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
    print ('1 nota de 5')
elif numero== 8:
    print ('1 nota de 5')
elif numero== 7:
    print ('1 nota de 5')
elif numero== 6:
    print ('1 nota de 5')
elif numero== 5:
    print ('1 nota de 5')
elif numero== 4:
    print ('0 notas de 5')
elif numero== 3:
    print ('0 notas de 5')
elif numero== 2:
    print ('0 notas de 5')
elif numero== 1:
    print ('0 nota de 5')
elif numero== 0:
    print ('0 notas de 5')



if numero== 9:
    print ('5 notas de 1')
elif numero== 8:
    print ('3 notas de 1')
elif numero== 7:
    print ('2 notas de 1')
elif numero== 6:
    print ('1 notas de 1')
elif numero== 5:
    print ('0 notas de 1')
elif numero== 4:
    print ('4 notas de 1')
elif numero== 3:
    print ('3 notas de 1')
elif numero== 2:
    print ('2 notas de 1')
elif numero== 1:
    print ('1 nota de 1')
elif numero== 0:
    print ('0 notas de 1')