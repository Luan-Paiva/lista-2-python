#Faça um programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

sexo = input("Digite F para feminino ou M para masculino: ")
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else:
    print("Sexo Inválido")