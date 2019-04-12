#Exercício 1.4. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os
#valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
#isósceles ou escaleno. Dicas:
#• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#•Triângulo Equilátero: três lados iguais;
#• Triângulo Isósceles: quaisquer dois lados iguais;
#• Triângulo Escaleno: três lados diferentes;

ladoX = float(input("Digite o primeiro lado:"))
ladoY = float(input("Digite o segundo lado:"))
ladoZ = float(input("Digite o terceiro lado:"))


if ladoX > (ladoY + ladoZ) or ladoY > (ladoX + ladoZ) or ladoZ > (ladoX + ladoY):
    print("Não é um triangulo")
elif ladoX == ladoY == ladoZ:
    print("Triângulo Equilátero")
elif ladoX == ladoY or ladoX == ladoZ or ladoY == ladoZ:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")