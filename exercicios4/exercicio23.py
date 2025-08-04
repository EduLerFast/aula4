"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento."""

try:
 valor= int(input('coloque um numero'))
 if valor:
   print ('o numero é inteiro')
except ValueError as e:#Nao consegui fazer com a funçao de arredondamento:(
  print ('o numero é decimal')


