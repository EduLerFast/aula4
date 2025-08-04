"""

    O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.

Confira:

Até 5 Kg:

    File Duplo R$ 4,90 por Kg
    Alcatra R$ 5,90 por Kg
    Picanha R$ 6,90 por Kg

Acima de 5 Kg:

    File Duplo R$ 5,80 por Kg
    Alcatra R$ 6,80 por Kg
    Picanha R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
 Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
   usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

fileduplo= float(input ("quantos quilos de file duplo deseja comprar?:"))
alcatra= float(input ("quantos quilos alcatra deseja comprar?:"))
picanha= float(input ("quantosquilos picanha deseja comprar?:"))
cartao= (input ("possui o cartao tabajara?:")).lower()

valor=0
if cartao==('sim'):
 valor=  valor+1
elif cartao==('nao'):
 valor=  valor+0

preco5fi=fileduplo*4.90
preco5al=alcatra*5.90
preco5pi=picanha*6.90

discontocarne5=(preco5fi+preco5al+preco5pi)*0.05
print (discontocarne5)
preco6fi=fileduplo*5.80
preco6al=alcatra*6.80
preco6pi=picanha*7.80 

discontocarne6=(preco6fi+preco6al+preco6pi)*0.05
print (discontocarne6)




#N SEI SE TA CORRETO

if valor==1  and fileduplo + alcatra + picanha <= 5:                                            
  print (f'foram selecionados {fileduplo+alcatra+picanha:.2f}quilos de carne\n {fileduplo} File Duplo \n {alcatra} Alcatra \n {picanha} Picanha\npreço total:R${preco5fi+preco5al+preco5pi:.2f}\n pagamento no cartão\n valor do desconto {(preco5fi+preco5al+preco5pi)*0.05:.2f} \n valor a pagar:R${(preco5fi+preco5al+preco5pi)-discontocarne5:.2f} ')                        


elif valor==0 and fileduplo + alcatra + picanha  <= 5:
 print (f'foram selecionados {fileduplo+alcatra+picanha:.2f}quilos de carne\n {fileduplo} File Duplo \n {alcatra} Alcatra \n {picanha} Picanha\npreço total:R${preco5fi+preco5al+preco5pi:.2f}\n pagamento no dinheiro\n valor do desconto {(preco5fi+preco5al+preco5pi)*0:.2f} \n valor a pagar:R${(preco5fi+preco5al+preco5pi):.2f} ')







elif valor==1  and fileduplo + alcatra + picanha > 5:                                            
 print (f'foram selecionados {fileduplo+alcatra+picanha:.2f}quilos de carne\n {fileduplo} File Duplo \n {alcatra} Alcatra \n {picanha} Picanha\npreço total:R${preco6fi+preco6al+preco6pi:.2f}\n pagamento no cartão\n valor do desconto {(preco6fi+preco6al+preco6pi)*0.05:.2f} \n valor a pagar:R${(preco6fi+preco6al+preco6pi)-discontocarne6:.2f} ')
                 

elif valor==0 and fileduplo + alcatra + picanha  > 5:
 print (f'foram selecionados {fileduplo+alcatra+picanha:.2f}quilos de carne\n {fileduplo} File Duplo \n {alcatra} Alcatra \n {picanha} Picanha\npreço total:R${preco6fi+preco6al+preco6pi:.2f}\n pagamento no dinheiro\n valor do desconto {(preco6fi+preco6al+preco6pi)*0:.2f} \n valor a pagar:R${(preco6fi+preco6al+preco6pi):.2f} ')











""""
elif morango + maca >5:
 preco6mo=morango*2.20
 preco6ma=maca*1.50
 #print ('preço',preco6mo+preco6ma)       
 precototal6=(preco6mo+preco6ma)
 if precototal6>=25 or morango + maca >=8:
  precototal6d=precototal6*0.10
  print (f'preço:R${precototal6-precototal6d:.2f}')
 """