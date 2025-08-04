"""
    Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se
      o mesmo é: equilátero, isósceles ou escaleno. Dicas:

    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

lado1= float (input('coloque o 1° lado:'))
lado2= float (input('coloque o 2° lado:'))
lado3= float (input('coloque o 3° lado:'))
tdslado= lado1 and lado2 and lado3
ladodiv=(lado1 and lado2 and lado3 / tdslado)-3
ladox3=tdslado+ tdslado
print (ladox3)


if lado1 == lado2 == lado3:
    print('seu triangulo é um equilatero')
    
elif lado1 + lado2 + lado3 != ladox3 :
    print('seu triangulo é um isoceles')

elif ladodiv==-2 :
    print('seu triangulo é um escaleno')

 

