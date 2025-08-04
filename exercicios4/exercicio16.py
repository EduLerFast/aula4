"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
 consistências, informando ao usuário nas seguintes situações:
 
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
a= float (input('coloque o valor do "A":'))
if a==0:
    print ('calculo encerrado')
else: 
    
 import math

 b= float (input('coloque o valor do "B":'))
 c= float (input('coloque o valor do "C":'))

 delta= (b**2) -4 * a * c
 bhaskaramais=(-b + math.sqrt(delta)) / (2*a)
 bhaskaramenos=(-b - math.sqrt(delta)) / (2*a)
 #print(delta)
 #print(bhaskaramais)
 #print(bhaskaramenos)
 if delta <0:
  print ('a equação não possui raizes reais')
 elif delta==0:


  print(f'a equação possui apenas uma raiz real;{bhaskaramais:.2f}')
 elif delta>= 0:
  print(f'a equação possui duas raiz reais;{bhaskaramais:.2f} e {bhaskaramenos:.2f}')