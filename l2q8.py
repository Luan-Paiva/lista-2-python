'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

valor_1 = float(input('Digite o primeiro número: '))
valor_2 = float(input('Digite o segundo número: '))
valor_3 = float(input('Digite o terceiro número: '))

if valor_1<valor_2 and valor_3:
    print('O produto mais barato é o primeiro produto')
elif valor_2<valor_3:
    print('O produto mais barato é o segundo produto')
else:
    print('O produto mais barato é o terceiro produto')