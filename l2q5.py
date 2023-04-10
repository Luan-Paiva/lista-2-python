"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada pelo aluno e apresentar:
  A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  A mensagem "Reprovado, se a média alcançada for menor que sete;
  A mensagem "Aprovado com Distinção" se a média alcançada for igual a dez.
  
  """
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
média = (nota_1 + nota_2) / 2

if média == 10:
      print("Aprovado com Diatinção:")
elif média >= 7:
    print("Aprovado")
else:
    print("Reprovado")