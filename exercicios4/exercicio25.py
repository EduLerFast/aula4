"""""
    Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""""


pergunta1= (input ("Telefonou para a vítima?:")).lower()
pergunta2= (input ("Esteve no local do crime?:")).lower()
pergunta3= (input ("Mora perto da vítima?:")).lower()
pergunta4= (input ("Devia para a vítima?:")).lower()
pergunta5= (input ("Já trabalhou com a vítima?:")).lower()

valor=0

if pergunta1==('sim'):
 valor=  valor+1
elif pergunta1==('nao'):
 valor=  valor+0

if pergunta2==('sim'):
 valor=  valor+1
elif pergunta2==('nao'):
 valor=  valor+0

if pergunta3==('sim'):
 valor=  valor+1
elif pergunta3==('nao'):
 valor=  valor+0

if pergunta4==('sim'):
 valor=  valor+1
elif pergunta4==('nao'):
 valor=  valor+0

if pergunta5==('sim'):
 valor=  valor+1
elif pergunta5==('nao'):
 valor=  valor+0


if valor==5:
    print('ASSASINO')
elif valor== 3 or valor== 4:
    print('Cúmplice')

elif valor==2:
    print('suspeito')
else:
    print ('inocente')


