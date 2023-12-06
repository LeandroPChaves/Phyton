'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
Unidade: 4, dezena: 3, centena: 8, milhar: 1'''

num = int(input('Digite um número inteiro entre 0 a 9999: '))
n = str(num)

#calculando como string, porém será necessário digitar de 1000 em diante.
'''print('Analisando o número informado: ')
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(n[3], n[2], n[1], n[0]))'''

#calculando como numérico.
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número informado: ')
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(u, d, c, m))

