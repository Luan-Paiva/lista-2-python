'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = str(input('Digite o turno em que você estuda e escolha "M", "V" ou "N": ')).strip().upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Bom dia!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Invalido!')