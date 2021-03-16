print('''Vamos trabalhar com números:''')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
escolha = 0

while escolha == 0:
    print('''O que você deseja fazer com esses termos?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior número
[ 4 ] Novos números
[ 5 ] Encerrar Programa''')
    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:  #SOMA
        print(f'A soma entre {num1} + {num2} = {num1 + num2}')
        print('-=' * 25)
        escolha = 0
    if escolha == 2:  #MULTIPLICAÇÃO
        print(f'A multiplicação entre {num1} X {num2} = {num1 * num2}')
        print('-=' * 25)
        escolha = 0
    if escolha == 3:  #MAIOR NÚMERO
        if num1 > num2:
            print(f'O maior número é {num1} e ele é o primeiro número.')
        if num2 > num1:
            print(f'O maior número é {num2} e ele é o segundo número.')
        if num1 == num2:
            print(f'O primeiro número é igual ao segundo número.')
        print('-=' * 25)
        escolha = 0
    if escolha == 4:  #NOVOS NÚMEROS
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('-=' * 25)
        escolha = 0
    if escolha == 5:  #ENCERRAR O PROGRAMA
        print('Encerrando o Programa...')
        break
    if escolha < 0 or escolha > 5:
        print('Opção incorreta, por gentileza, tente novamente.')
        escolha = 0

print('Programa Encerrado. Obrigado por usar nosso programa.')
