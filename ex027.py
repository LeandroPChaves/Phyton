'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

nome = input('Informe seu nome completo: ').strip()
nome = nome.split()
print('O primeiro nome é: {}' .format(nome[0]))
#print('O último nome é: {}' .format(nome[len(nome)]-1))



for x in range(nome.__len__()):
   if (x == nome.__len__() - 1):
       print('O último nome é: ' , nome[x])

