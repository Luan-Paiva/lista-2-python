'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule 
a sua média. A atribuição de conceitos obedece à tabela abaixo:
    ◦   Média de Aproveitamento  Conceito
        Entre 9.0 e 10.0        A
        Entre 7.5 e 9.0         B
        Entre 6.0 e 7.5         C
        Entre 4.0 e 6.0         D
        Entre 4.0 e zero        E
      O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito 
      for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

if ((nota_1 + nota_2)/2) >= 9 <=10:
    numero = '9.0 e 10.0'
    media = 'A'
    if media == 'A':
        mensagem = "APROVADO"
elif ((nota_1 + nota_2)/2) >= 7.5 <=9:
    numero = '7.5 e 9.0'
    media = 'B'
    if media == 'B':
        mensagem = "APROVADO"
elif ((nota_1 + nota_2)/2) >= 6 <=7.5:
    numero = '6.0 e 7.5'
    media = 'C'
    if media == 'C':
        mensagem = "APROVADO"
elif ((nota_1 + nota_2)/2) >= 4 <=6:
    numero = '4.0 e 6.0'
    media = 'D'
    if media == 'D':
        mensagem = "REPROVADO"
elif ((nota_1 + nota_2)/2) >= 0 <=4:
    numero = '0 e 4.0'
    media = 'E'
    if media == 'E':
        mensagem = "REPROVADO"
        
print(f'Média de Aproveitamento  Conceito\nNota entre {numero}       {media}')