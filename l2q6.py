""""Faça um programa que leia tres numeros e mostre o maior deles.

"""
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro numéro: "))
terceiro_numero = int(input("Digite mais um numéro: "))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero: 
    print(f"{segundo_numero: } foi o maior número digitado ")
    
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print(f"{segundo_numero: } foi o maior número digitado ")
else:
    print(f"{terceiro_numero: } foi o maior número digitado ")