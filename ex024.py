'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''

cidade = input('Digite o nome da cidade: ').strip().upper()

resposta = cidade.find('SANTO', 0)

'''while (cidade[0] == ' '):
    cidade = input('Digite o nome da cidade: ')'''

if (resposta == 0):
    print('A cidade começa com o nome Santo.')
else:
    print('A cidade não começa com o nome Santo.')










