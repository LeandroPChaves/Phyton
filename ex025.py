'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = input('Digite o nome completo: ').upper().strip()

#print ('Seu nome tem Silva? {}' .format('SILVA' in nome.upper()))

if (nome.find('SILVA') == -1):
    print('{} não tem Silva no nome' .format(nome))
else:
    print('{} tem Silva no nome' .format(nome))