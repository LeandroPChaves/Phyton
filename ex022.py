'''Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas minúsculas.
* Quantas letras ao todo sem considerar espaços.
* Quantas letras tem o primeiro nome.'''

nome = input('Informe o nome completo: ').strip()
print('Maiúscula: ', format(nome.upper()))
print('Minúscula: ', format(nome.lower()))
nome = nome.split()
contador = 0
for x in range(nome.__len__()):
    contador = contador + nome[x].__len__()
print('Quantidade Total de letras sem contar espaço: ', format(contador))
print('Quantidade de letras do primeiro nome: ', format(nome[0].__len__()))

#Eu poderia eliminar o for range usando no print do for: .format(len(nome)-nome.count(' '))






