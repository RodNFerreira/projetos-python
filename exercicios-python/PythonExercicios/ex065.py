resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Acabou.')
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior número que você digitou foi {maior}, e o menor {menor}.')
