''' Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    ◦ Dicas:
    ◦ Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    ◦ Triângulo Equilátero: três lados iguais;
    ◦ Triângulo Isósceles: quaisquer dois lados iguais;
    ◦ Triângulo Escaleno: três lados diferentes;'''
    
lado_1 = float(input('Iforme o primeiro lado do triangulo: '))
lado_2 = float(input('Iforme o primeiro lado do triangulo: '))
lado_3 = float(input('Iforme o primeiro lado do triangulo: '))
if lado_1 == lado_2 and lado_1 == lado_3:
    valor = 'EQUILÁTERO'
elif lado_1 != lado_2 and lado_1 == lado_3:
    valor = 'ISÓSCELES'
elif lado_1 != lado_3 and lado_1 == lado_2:
    valor = 'ISÓSCELES'
elif lado_2 != lado_1 and lado_2 == lado_3:
    valor = 'ISÓSCELES'
elif lado_1 != lado_2 and lado_1 != lado_3:
    valor = 'ESCALENO'
print(f'Os valores informam que o seu triângulo é {valor}')