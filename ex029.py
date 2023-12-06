'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = int(input('Informe a velocidade do carro: Km '))
excesso = 0

if (velocidade > 80):
    excesso = velocidade - 80
    multa = excesso * 7
    print(' Velocidade atual: {}Km \n Velocidade excedida em {}km \n Pague R${} de multa' .format(velocidade, excesso, multa))
else:
    print('Velocidade permitida')