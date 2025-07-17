#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
fm=  (input  ('coloque F caso feminino ou M caso masculino:'))
if fm==('F'):# nao consegui usar .lower
    print('Feminino')
elif fm==('M'):
    print('Masculino')
else:
    print('sexo invalido')
