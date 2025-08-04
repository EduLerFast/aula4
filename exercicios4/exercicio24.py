"""
    Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""#incompleto:(
valor1= int(input('coloque um numero:'))
valor2= int(input('coloque outro numero:'))

operacao= int(input('(1)inteiro ou decimal\n(2)positivo ou negativo\n(3)par ou ímpar\nqual operaçao deseja fazer?:'))
if operacao==2:

    if valor1 < 0 :
     print(f'o numero {valor1}  é negativo')
    else:
     print(f'o numero {valor1} é positivo')

    if valor2 < 0 and valor2 and operacao==2:
         print(f'o numero {valor2} é negativo')
    else:
         print(f'o numero {valor2} é positivo')


elif operacao==3:


    if valor1 % 2== 1:
     print(f'o numero {valor1} é impar')
    else :
       print(f'o numero {valor1} é par')


    if valor2 % 2== 1 and valor2 and operacao==3:
          print(f'o numero {valor2} é impar')
    else:
          print(f'o numero {valor2} é par')









elif operacao==1:

 try:

  if valor1 ==1:
   print (f'o numero {valor1} é inteiro')
 except ValueError as e:#Nao consegui fazer com a funçao de arredondamento:(
  print (f'o numero {valor1} é decimal')





 try:

  if valor2 and operacao==1:
   print (f'o numero {valor2} é inteiro')
 except ValueError as e:#Nao consegui fazer com a funçao de arredondamento:(
  print (f'o numero {valor2} é decimal')


