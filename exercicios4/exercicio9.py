#Faça um Programa que leia três números e mostre-os em ordem decrescente.
Numero1= float (input  ('coloque um numero:'))
Numero2= float (input  ('coloque outro numero:'))#incompleto
Numero3= float (input  ('coloque outro numero:'))
if   Numero1 > (Numero2 and Numero3):
    print (f'{Numero1} é o maior numero')

elif Numero2 > (Numero1 and Numero3):
    print (f'{Numero2} é o maior numero')

elif Numero3 > (Numero1 and Numero2):
    print (f'{Numero3} é o maior numero')


try:
 if Numero1 > Numero2  < Numero3:
    print (f'{Numero1} é o numero do meio')

 elif Numero2 > Numero3 < Numero1:
    print (f'{Numero1} é o numero do meio')

 elif Numero3 > Numero2 < Numero1:
    print (f'{Numero1} é o numero do meio')
except:
   print (Numero1 or Numero2 or Numero3)




    

if   Numero1 < (Numero2 and Numero3):
    print (f'{Numero1} é o menor numero')

elif Numero2 < (Numero1 and Numero3):
    print (f'{Numero2} é o menor numero')

elif Numero3 < (Numero1 and Numero2):
    print (f'{Numero3} é o menor numero')