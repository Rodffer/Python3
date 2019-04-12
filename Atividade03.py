#Exercício 1.3. As Organizações Tabajara resolveram dar um aumento de salário aos 
# seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
#• salários até R$ 280,00 (incluindo) : aumento de 20%
#• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#• salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:
#• o salário antes do reajuste;
#• o percentual de aumento aplicado;
#• o valor do aumento;
#• o novo salário, após o aumento.

salario_colaborador = float(input("Digite seu salario:..."))

if salario_colaborador < 280.00:
        salario_reajuste = salario_colaborador + 0.20*salario_colaborador
        valor_aumentado = 0.20*salario_colaborador
        print(f"Salario antes do reajuste : {salario_colaborador}")
        print("Percentual de aumento: 20%")
        print(f"Valor aumentado: {valor_aumentado:.2f}")
        print(f"Salario com aumento: {salario_reajuste:.2f}")
elif salario_colaborador > 280.00 and salario_colaborador < 700.00:
        salario_reajuste = salario_colaborador + 0.15*salario_colaborador
        valor_aumentado = 0.15*salario_colaborador
        print(f"Salario antes do reajuste : {salario_colaborador}")
        print("Percentual de aumento: 15%")
        print(f"Valor aumentado: {valor_aumentado:.2f}")
        print(f"Salario com aumento: {salario_reajuste:.2f}")
elif salario_colaborador > 700.00 and salario_colaborador < 1500.00:
        salario_reajuste = salario_colaborador + 0.10*salario_colaborador
        valor_aumentado = 0.10*salario_colaborador
        print(f"Salario antes do reajuste : {salario_colaborador}")
        print("Percentual de aumento: 10%")
        print(f"Valor aumentado: {valor_aumentado:.2f}")
        print(f"Salario com aumento: {salario_reajuste:.2f}")
elif salario_colaborador > 1500.00:
        salario_reajuste = salario_colaborador + 0.05*salario_colaborador
        valor_aumentado = 0.05*salario_colaborador
        print(f"Salario antes do reajuste : {salario_colaborador}")
        print("Percentual de aumento: 5%")
        print(f"Valor aumentado: {valor_aumentado:.2f}")
        print(f"Salario com aumento: {salario_reajuste:.2f}")
else:
    print("Entrada incorreta")