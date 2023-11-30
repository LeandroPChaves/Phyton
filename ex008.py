#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

numero = int(input('Digite um número'))
centimetros = numero * 100
milimetros = numero * 1000

print (' {} em centímetros é: {} \n {} em milimetros é: {}.' .format(numero, centimetros, numero, milimetros))