'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é
descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    ◦ Desconto do IR:
    ◦ Salário Bruto até 900 (inclusive) - isento
    ◦ Salário Bruto até 1500 (inclusive) - desconto de 5%
    ◦ Salário Bruto até 2500 (inclusive) - desconto de 10%
    ◦ Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
              Salário Bruto: (5 * 220)        : R$ 1100,00
              (-) IR (5%)                     : R$   55,00  
              (-) INSS ( 10%)                 : R$  110,00
              FGTS (11%)                      : R$  121,00
              Total de descontos              : R$  165,00
              Salário Liquido                 : R$  935,00'''
              
print('~FOLHA DE PAGAMENTO~')   
valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
quantidade_horas_trabalho = float(input('Digite a quantidade de horas que você trabalhou: '))
salario = valor_hora * quantidade_horas_trabalho

if salario <= 900:
    IR = 0
    INSS = 0
    FGTS = salario - ((11/100) * salario)
    salario_liquido = salario - (((10/100) + (5/100)) * salario)
    total_descontos = ((IR + salario) + salario ) - salario 
elif salario  >= 900 and salario <= 1500:
    IR = salario - ((5/100) * salario)
    INSS = 0
    FGTS = salario - ((11/100) * salario)
    salario_liquido = salario - (((10/100) + (5/100)) * salario)
    total_descontos = (salario - IR) - INSS 
elif salario >= 1501 and salario <= 2500:
    IR = 0
    INSS = salario - ((10/100) * salario)
    FGTS = salario - ((11/100) * salario)
    salario_liquido = salario - (((10/100) + (5/100)) * salario)
    total_descontos = (salario - IR) - INSS
elif salario >= 2500:
    IR = 0
    INSS = 0 
    desconto = salario - ((20/100) * salario)
    FGTS = salario - ((11/100) * salario)
    salario_liquido = salario - (((10/100) + (5/100)) * salario)
    total_descontos =  ((salario - IR) - INSS) - desconto

print(f'Salário Bruto: ({quantidade_horas_trabalho:.2f} * {valor_hora:.2f})               : R${salario:.2f}')
print(f'IR (5%)                         : R${IR}')
print(f'INSS ( 10%)                     : R${INSS}')
print(f'FGTS (11%)                      : R${FGTS}')
print(f'Total de descontos              : R${total_descontos}')
print(f'Salário Liquido                 : R${salario_liquido}')