'''Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM
para viagens de até 200km e R$0,45 para viagens mais longas.'''

distancia = float(input('Informe a distância da viagem em km: '))

while distancia < 0:
    distancia = float(input('Informe a distância da viagem em km: '))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O valor total da passagem é: R${:.2f}' .format(passagem))

#passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
