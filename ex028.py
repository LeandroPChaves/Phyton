'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randrange
from time import sleep

#Além do randrange, eu poderia usar o randint, ambos da biblioteca random.
#O Sleep é para demorar a carregar. escolhemos o tempo de espera.

sorteio = randrange(1,6)
print('--------Tente adivinhar o número sorteado pelo computador ------------')

numero = int(input('Digite um número entre 1 e 5 '))

while(numero < 1) or (numero > 5):
    numero = int(input('Digite um número entre 1 e 5'))

if (numero == sorteio):
    print('PROCESSANDO...')
    sleep(2)
    print('Você acertou: O número sorteado é {} ' .format(sorteio))
else:
    print('PROCESSANDO...')
    sleep(2)
    print('Você errou: O número sorteado é: {} ' .format(sorteio))







