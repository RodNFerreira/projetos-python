frase = str(input('Digite uma frase:')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A letra A aparece a primeira vez na posição {frase.find("A")}')
print(f'A última letra A apareceu na posição {frase.rfind("A")}')
