'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
 
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

if numero_1 > numero_2 and  numero_1 > numero_3:
    maior = numero_1
    if numero_2 > numero_3:
        medio = numero_2
        menor = numero_3
    else:
        medio = numero_3
        menor = numero_2
elif numero_2 > numero_3 and numero_2 > numero_1:
    maior = numero_2
    if numero_3 > numero_1:
        medio = numero_3
        menor = numero_1
    else:
        medio = numero_1
        menor = numero_3
elif numero_3 > numero_2 and numero_3 > numero_1:
    maior = numero_3
    if numero_2 > numero_1:
        medio = numero_2
        menor = numero_1
    else:
        medio = numero_1
        menor = numero_2
print(f'O maior número é {maior}')
print(f'O número do meio é {medio}')
print(f'O menor número é {menor}')
