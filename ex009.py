#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('A tabuada de qual número o sr(a) deseja visualizar?'))
contador = 1
resultado = 0

print('-' * 12)

while contador < 11:
    resultado = num * contador
    print(num ,'*', contador, '=', resultado)
    contador += 1

print('-' * 12)