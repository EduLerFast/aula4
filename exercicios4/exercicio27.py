"""
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg:

    Morango R$ 2,50 por Kg
    Maçã R$ 1,80 por Kg

Acima de 5 Kg:

    Morango R$ 2,20 por Kg

    Maçã R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
 Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morango= float(input ("quantos Kg de morangos deseja comprar?:"))
maca= float(input ("quantos Kg maçãs deseja comprar?:"))

#N SEI SE TA CORRETO
if morango + maca <= 5:
 preco5mo=morango*2.50
 preco5ma=maca*1.80
 print ('preço:R$',preco5mo+preco5ma)
 precototal5=(preco5mo+preco5ma)#acho q essa parte aqui é meio inutil#######
 if precototal5>=25 or morango + maca >=8:                                 #
  precototal5d=precototal5*0.10                                            #
  print (f'preço:R${precototal5-precototal5d:.2f}')                        #
############################################################################


elif morango + maca >5:
 preco6mo=morango*2.20
 preco6ma=maca*1.50
 #print ('preço',preco6mo+preco6ma)         <---#inutilizado
 precototal6=(preco6mo+preco6ma)
 if precototal6>=25 or morango + maca >=8:
  precototal6d=precototal6*0.10
  print (f'preço:R${precototal6-precototal6d:.2f}')
 