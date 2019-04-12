#A série de Fibonacci é formada pela sequência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, .... 
# Faça um programa que gere a série até que o valor seja maior que 500.
def fibonacci(n):
    num1 = 0
    num2 = 1
    print(num1)
    while (num2 <= n):
        soma = num1
        num1 = num2
        num2 = num1 + soma
        print(num1)

fibonacci(620)