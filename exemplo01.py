#Converter Celsius em Fahrenheint 
#Converter Fahrenheint em Celsius

def c_f(c):
    return (9.0 / 5) * c + 32


def f_c(f):
    return (5 * (f - 32)) / 9


entradaC_f = float(input('Digite um número em Celsius: '))
print(entradaC_f, 'em fahrenheint: ', c_f(entradaC_f))

entradaF_c = float(input('Digite um Número em Fahrenheint: '))
print((entradaF_c, 'em celsius: ', f_c(entradaF_c)))
