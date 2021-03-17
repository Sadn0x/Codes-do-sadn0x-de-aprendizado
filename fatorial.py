from math import factorial
fat = int(input('Digite um número para calcular seu fatorial: '))
c = fat

print(f'Calculando {fat}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else f' = {factorial(fat)}', end='')
    c -= 1
