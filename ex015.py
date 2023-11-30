#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input('Informe quantidade de KM`s percorridos: '))
dias = int(input('Informe quantidade de dias do aluguel: '))
valordias = dias * 60
valorkm = km * 0.15
pagamento = valordias + valorkm

print (' O carro foi utilizado por {} dias e rodou {:.2f} km´s. \n O valor total a pagar é: R$ {:.2f}.' .format(dias, km, pagamento))