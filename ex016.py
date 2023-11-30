#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua parte inteira.

import math

num = float(input('Digite um número real qualquer: '))

resposta = math.floor(num)

print ('O número real digitado convertido para inteiro é: {}' .format(resposta))