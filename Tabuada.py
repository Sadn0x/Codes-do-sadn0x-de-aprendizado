print('-'*5, 'Vamos fazer uma tabuada.', '-'*5)

print('''Digite dentre as opções abaixo, qual tabuada você quer ver:
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO''')

tabuada = int(input('Digite a sua opção: '))

while tabuada < 1 or tabuada > 4:
    print('OPÇÃO INCORRETA, TENTE NOVAMENTE')
    tabuada = int(input('Digite a sua opção: '))



if tabuada == 1:
    print('Você escolheu a tabuada de SOMA')
    n = int(input('Digite um número para vê sua tabuada: '))
    for d in range(1, 11):
        print('-=' * 5, 'Tabuada de Soma: ', '-=' * 5)
        print('{} + {} = {}'.format(n, d, n + d))
if tabuada == 2:
    print('Você escolheu a tabuada de SUBTRAÇÃO')
    n = int(input('Digite um número para vê sua tabuada: '))
    for f in range(1, 11):
        print('-=' * 5, 'Tabuada de Subtração: ', '-=' * 5)
        print('{} - {} = {}'.format(n, f, n - f))
if tabuada == 3:
    print('Você escolheu a tabuada de MULTIPLICAÇÃO')
    n = int(input('Digite um número para vê sua tabuada: '))
    for c in range(1, 11):
        print('-=' * 5, 'Tabuada de Multiplicação: ', '-=' * 5)
        print('{} * {} = {}'.format(n, c, n * c))
if tabuada == 4:
    print('Você escolheu a tabuada de DIVISÃO')
    n = int(input('Digite um número para vê sua tabuada: '))
    for e in range(1, 11):
        print('-=' * 5, 'Tabuada de Divisão: ', '-=' * 5)
        print('{} / {} = {}'.format(n, e, n / e))
