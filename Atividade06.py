#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva 
# uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

dia = int(input("Digite o dia:"))
mes = int(input("Digite o mes:"))
ano = int(input("Digite o ano:"))

def dia_texto(dia):
	lista_de_dia = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorzer", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte", "Vinte e Um", "Vinte e Dois", "Vinte e Três", "Vinte e Quatro", "Vinte e Cinco", "Vinte e Seis", "Vinte e Sete", "Vinte e Oito", "Vinte e Nove", "Trinta", "Trinta e Um"]
	texto_dia = lista_de_dia[dia-1]
	return texto_dia

def mes_texto(mes):
	lista_de_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	texto_mes = lista_de_mes[mes-1]
	return texto_mes

print("O valor por extenso é " + dia_texto(dia) + " de " + mes_texto(mes) + " de %i "%ano)