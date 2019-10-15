print("########################")
print("#####NÚMERO#SECRETO#####")
print("########################")

adivinha = 27

palpite_str = input("Qual o numero secreto?")

print("Seu Palpite:", palpite_str)

palpite = int(palpite_str)

acertou = adivinha == palpite
maior = palpite > adivinha
menor = palpite < adivinha

if(acertou):
    print("######!!ACERTOU!!#######")
    print("##########", adivinha, "##########")
else:
    print("########ERROU###########")
    if(maior):
        print("Palpite MAIOR do que o\n número Secreto")
    elif (menor):
        print("Palpite MENOR do que o\n número Secreto")
print("########################")