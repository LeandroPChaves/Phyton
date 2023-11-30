#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

dinheiro = float(input('Quanto dinheiro há na sua carteira? R$ '))
conversao = dinheiro / 3.27

print('Com R${}, você pode comprar ${:.2f}' .format(dinheiro, conversao))