n = input('Digite algo: ')
print(n, 'É do tipo primitivo: ', type(n))
print(n, 'Possui letras ou números? ', n.isalnum())
print(n, 'Possui apenas letras? ', n.isalpha())
print(n, 'Está tudo em minúsculo? ', n.islower())
print(n, 'Possui apenas números? ', n.isnumeric())
print(n, 'Está tudo em maiúsculo? ', n.isupper())
