"""
    Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento

    Entre 9.0 e 10.0 : A
    Entre 7.5 e 9.0 : B
    Entre 6.0 e 7.5 : C
    Entre 4.0 e 6.0 : D
    Entre 4.0 e zero : E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota1= float (input('coloque sua 1° nota:'))
                                                                    
nota2= float (input('coloque sua 2° nota:'))

media= (nota1 + nota2)/2 

print(f'sua media é: {media:.1f}')

if media  <4  :
          print('E')
elif media  <6  : 
       print('D')
elif media  <7.5  : 
       print('C')
elif media  <9  : 
       print('B')
elif media  >= 9  : 
       print('A')





"""if media >=  9 :
 print('A')

elif media< 9.0  > 7.5:
     print('B')
elif media < 7.5 > 6.0  :
     print('C')

elif media < 6.0 > 4.0 : 
       print('D')
   
elif media < 4.0 > -1:
          print('E')
          """
