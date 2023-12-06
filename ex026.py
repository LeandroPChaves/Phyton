'''Faça um programa que leia uma frase pelo teclado e mostre:
* Quantas vezes aparece a letra "A"
* Em que posição ela aparece a primeira vez.
* Em que posição ela aparece a última vez.'''
import random

frase = input('Digite uma frase: ').upper().strip()
print('A quantidade da letra A na frase é: {} '.format(frase.count('A')))
print('A posição da primeira letra A na frase é: {} '.format(frase.find('A',0)))
print('A posição da última letra A na frase é: {} '.format(frase.rfind('A')))


