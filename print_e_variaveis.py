#Print PY
print("teste")
print("RR", 1, "RRR", 3, sep="\n")
print("RR", 3, "RRR", 3, end="\n")

#sep é o separador entre os valores, por padrão o separador é um espaço em branco.
#end é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (\n).
#O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis (ou identificadores).
valor_da_compra = 20
nome_cliente = 'João José'
parcelas_a_receber = 5

x = 10
y = 20

print("Cliente:", nome_cliente, "\n", "Valor:", valor_da_compra, "\n", "Parcelas:", parcelas_a_receber)

print(x+y)
print(y-x)
print(x*y)
print(x/y)