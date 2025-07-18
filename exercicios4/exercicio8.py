#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1= float (input  ('qual o preço do produto?:'))
produto2= float (input  ('qual o preço de outro produto?:'))
produto3= float (input  ('qual o preço de outro produto?:'))

if   produto1 < (produto2 and produto3):
    print (f'compre o produto que custa', produto1)

elif produto2 < (produto1 and produto3):
    print (f'compre o produto que custa', produto2)

elif produto3 < (produto1 and produto2):
    print (f'compre o produto que custa', produto3)