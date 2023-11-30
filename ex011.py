#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2mª.

largura = float(input('Digite a largura da parede'))
altura = float(input('Digite a altura da parede'))
area = largura * altura
tinta = area / 2

print ('A área da parede em metros quadrados é: {:.2f} e a quantidade de litro de tinta necessária é: {:.2f}' .format(area, tinta))