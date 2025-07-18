#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

"""A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""



nota1= float (input('coloque sua 1° nota:'))
                                                                    
nota2= float (input('coloque sua 2° nota:'))

media= (nota1 + nota2)/2 

print(f'sua media é: {media:.1f}')

if media > 9 :
     print('Aprovado com Distinção')

elif media < 7:
    print ('reprovado')

elif media > 7 <9 :
    print ('Aprovado')

    
