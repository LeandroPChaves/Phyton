#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
#Quadrado da hipotenusa é igual a soma dos quadrados dos catetos

oposto = float(input('Informe a medida do cateto oposto: '))
adjacente = float(input('Informe a medida do cateto adjacente: '))
hipotenusa = (oposto**2) + (adjacente**2)
hipotenusa = hipotenusa**0.5

print('A medida da hipotenusa é: {}' .format(hipotenusa))
