#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Se eu importasse somente os métodos utilizados da biblioteca math: from math import radians, sin, cos, tan. e tiraria o math dos códigos.
import math
angulo = float(input('Digite a medida do ângulo'))

seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(angulo, tangente))
