#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário do Funcionário: R$ '))
aumento = salario * (15/100)
salarioatual = salario + aumento

print ('O salário atualizado é: R$ {:.2f}' .format(salarioatual))