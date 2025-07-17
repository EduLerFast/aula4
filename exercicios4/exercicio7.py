#Faça um Programa que leia três números e mostre o maior e o menor deles.
Numero1= float (input  ('coloque um numero:'))
Numero2= float (input  ('coloque outro numero:'))
Numero3= float (input  ('coloque outro numero:'))
if Numero1 > Numero2 and Numero3:
 print (f'{Numero1} é o maior numero')

elif Numero2 > Numero1 and Numero3:
    print (f'{Numero2} é o maior numero')

elif Numero3 > Numero1 and Numero2:
    print (f'{Numero3} é o maior numero')

    

if Numero1 < Numero2 and Numero3:
    print (f'{Numero1} é o menor numero')

elif Numero2 < Numero1 and Numero3:
    print (f'{Numero2} é o menor numero')

elif Numero3 < Numero1 and Numero2:
    print (f'{Numero3} é o menor numero')