#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número'))
antecessor = num - 1
sucessor = num + 1

print(' O sucessor de {} é: {}. \n O antecessor de {} é: {}.' .format(num, sucessor, num, antecessor))