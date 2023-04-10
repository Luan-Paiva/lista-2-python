'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

numero_um = int(input('Digite o número um: '))
numero_dois = int(input('Digite o número dois: '))
numero_tres = int(input('Digite o número três: '))

if numero_um > numero_dois and numero_um > numero_tres:
    # print(numero_um)
    maior = numero_um
    if numero_dois > numero_tres:
        menor = numero_tres
    else:
        menor = numero_dois
elif numero_dois > numero_tres and numero_dois > numero_um:
    # print(numero_dois)
    maior = numero_dois
    if numero_um > numero_tres:
        menor = numero_tres
    else:
        menor = numero_um
else:
    # print(numero_tres)
    maior = numero_tres
    if numero_um > numero_dois:
        menor = numero_dois
    else:
        menor = numero_um

print(f'O maior é {maior} e o menor é {menor}')