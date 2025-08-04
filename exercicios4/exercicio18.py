#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia= int (input(f'coloque o dia dd/mm/aaaa:'))
mes= int (input(f'coloque o mes {dia}/mm/aaaa:'))
ano= int (input(f'coloque o ano {dia}/{mes}/aaaa:'))
print(f'data= {dia}/{mes}/{ano}:')

if   mes ==1 :
    print (dia<=31)
elif mes ==2 :
      print (dia<=28 or 29 )
elif mes ==3 :
      print (dia<=31, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==4 :
      print (dia<=30, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==5 :
      print (dia<=31, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==6 :
      print (dia<=30, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==7 :
      print (dia<=31, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==8 :
      print (dia<=31, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==9 :
      print (dia<=30, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==10 :
      print (dia<=31, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==11 :
      print (dia<=30, mes<=12, ano<=9999,  '\ndata valida')
elif mes ==12 :
      print (dia<=31, mes<=12, ano<=9999,  '\ndata valida')

else :
 print('data invalida')
