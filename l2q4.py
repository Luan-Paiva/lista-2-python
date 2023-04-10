#Faça um programa que diga se uma letra é vogal ou consoante.

letra = input("Digite uma letra: ").upper()

if (
    letra == "A"
    or letra == "E"
    or letra == "I"
    or letra == "O"
    or letra == "U"
):
    print("Vogal")
else:
    print("Consoante")