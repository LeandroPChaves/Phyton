#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o prelo do produto'))
desconto = preco * (5/100)
novopreco = preco - desconto

print(novopreco)