#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
#  mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno= (input  ('em que turno voce estuda'))

if turno=='M':
 print ('bom dia')

elif turno=='V':
 print ('boa tarde')

elif turno=='N':
 print ('boa noite')
else:
 print ('Valor invalido')