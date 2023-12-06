#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
numeros = [num1, num2, num3]
i = 0
maior = numeros[0]
menor = numeros[0]

while i < 3:
    atual = numeros[i]
    if atual > maior:
        maior = atual
    if atual < menor:
        menor = atual
    i += 1
if maior == menor:
    print('Números iguais')
else:
    print('O maior número digitado é: {} '.format(maior))
    print('O menor número digitado é: {} '.format(menor))