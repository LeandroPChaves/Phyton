algo = input('Digite Algo: ')

print(type(algo))

print('É caracter? ' , algo.isalpha())
print('É alfa numérico? ' , algo.isalnum())
print('As letras são minúsculas? ' , algo.islower())
print('As letras são maiúsculas? ' , algo.isupper())
print('É numérico? ' , algo.isnumeric())
print('É decimal? ', algo.isdecimal())