#Exercício 1.1. Tendo como dado de entrada a altura (h) de uma pessoa
#construa um algoritmo que calcule seu
#peso ideal, utilizando as seguintes fórmulas:
#a) Para homens: (72.7*h) - 58
#b) Para mulheres: (62.1*h) - 44.7

def calcula_homem (h):
     return((72.7*h) - 58)

def calcula_mulher (h):
    return((62.1*h) - 44.7)

h = float(input("Digite a altura..."))
g = input("Digite o genero M ou F...")
 
if g == 'M':
    peso_ideal_homem = calcula_homem(h)
    print(peso_ideal_homem)
elif g == 'F':
    peso_ideal_mulher = calcula_mulher(h)
    print(peso_ideal_mulher)
    pass
else:
    print("Informação digitada incorreta")
    pass

