"""Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

salario= float ( input ('qual seu salario:'))


if salario < 280.00 or 280.00 :
    print (f'seu salario é:{salario * 1.2}' )

elif salario > 280.00 < 700.00: 
    print (f'seu salario é:{salario * 1.15}' )

elif salario  > 700.00 < 1500: 
    print (f'seu salario é:{salario * 1.1}' )

elif salario  > 1500.00:
    print (f'seu salario é:{salario * 1.05}' )
