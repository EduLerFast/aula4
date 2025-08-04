#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano= float (input('coloque o ano:'))
anoc=ano/4

if anoc== int:
 print ('seu ano é bissexto')

else:
 print ('seu ano NAO é bissexto')
    