#Exercício 1.2. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
#no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
#11% para o Imposto de Renda, 
#8% para o INSS 
#e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.
#b) quanto pagou ao INSS.
#c) quanto pagou ao sindicato.
#d) o salário líquido.

ganha_por_hora = float(input("Quanto voce ganha por hora?"))
horas_por_mes = float(input("Quantas horas voce trabalha por mes?"))


def salario_bruto(ganha_por_hora, horas_por_mes):
    return(ganha_por_hora*horas_por_mes)
salario_b = salario_bruto(ganha_por_hora, horas_por_mes)

def valor_INSS(salario_b):
    return(0.08*(salario_b))
pagou_inss = valor_INSS(salario_b)

def valor_SINDICATO(salario_b):
    return(0.05*(salario_b))
pagou_sindicato = valor_SINDICATO(salario_b)
pagou_IR = (0.11*salario_b)

def salario_liquido(salario_b, pagou_inss, pagou_sindicato, pagou_IR):
    descontos = (pagou_inss + pagou_sindicato + pagou_IR)
    return(salario_b - descontos )
salario_final = salario_liquido(salario_b, pagou_inss, pagou_sindicato, pagou_IR)

print(f'Salario Bruto: R${salario_b:.2f}')
print(f'Valor pago ao INSS: R${pagou_inss:.2f}')
print(f'Valor pago ao Sindicato: R${pagou_sindicato:.2f}')
print(f'Salario Liquido: R${salario_final:.2f}')
