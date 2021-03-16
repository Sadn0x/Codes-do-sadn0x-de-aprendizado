import math

print('-=' * 5, 'BEM VINDO A CALCULADORA DO SADN0X', '-=' * 5)

escolha = 0
while escolha == 0:
    print('''Escolha a opção abaixo na qual precisará da calculadora:
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO
[ 5 ] RAIZ QUADRADA
[ 6 ] CÁLCULO EXPONÊNCIAL 
''')
    escolha = int(input('Digite uma opção: '))

    if escolha < 1 or escolha > 6:
        print('OPÇÃO INCORRETA, TENTE NOVAMENTE!')
        escolha = int(input('Digite a sua escolha: '))

    if escolha == 1:  # CALCULADORA DE SOMA
        print('Você escolheu a função de SOMA, da nossa calculadora, a seguir, digite os termos que deseja somar:')
        t1 = float(input('TERMO 1: '))
        t2 = float(input('TERMO 2: '))
        print(f'A soma entre o {t1} + {t2} = {t1 + t2}')

    if escolha == 2:  # CALCULADORA DE SUBTRAÇÃO
        print('Você escolheu a função de SUBTRAÇÃO, da nossa calculadora, a seguir, digite os termos que deseja subtrair:')
        t1 = float(input('TERMO 1: '))
        t2 = float(input('TERMO 2: '))
        print(f'A subtração entre o {t1} - {t2} = {t1 - t2}')
    if escolha == 3:  # CALCULADORA DE MULTIPLICAÇÃO
        print(
            'Você escolheu a função de MULTIPLICAÇÃO, da nossa calculadora, a seguir, digite os termos que deseja multiplicar:')
        t1 = float(input('TERMO 1: '))
        t2 = float(input('TERMO 2: '))
        print(f'A multiplicação entre o {t1} X {t2} = {t1 * t2}')
    if escolha == 4:  # CALCULADORA DE DIVISÃO
        print('Você escolheu a função de DIVISÃO, da nossa calculadora, a seguir, digite os termos que deseja dividir:')
        t1 = float(input('TERMO 1: '))
        t2 = float(input('TERMO 2: '))
        print(f'A divisão entre o {t1} / {t2} = {t1 / t2}')
    if escolha == 5:  # CALCULADORA DE RAIZ QUADRADA
        print(
            'Você escolheu a função de calcular a RAIZ QUADRADA, da nossa calculadora, a seguir, digite o termo que deseja saber sua raiz quadrada: ')
        t1 = int(input('Digite o número que deseja saber a sua raiz: '))
        print(f'A raiz de {t1} é {math.sqrt(t1)}')
    if escolha == 6:  # CALCULADORA DE CÁLCULO EXPONÊNCIAL
        print(
            'Você escolheu a função de realizar um CÁLCULO EXPONÊNCIAL, da nossa calculadora, a seguir, digite um termo de base e um expoente: ')
        t1 = int(input('Digite o número que deseja usar como base do cálculo exponêncial: '))
        t2 = int(input('Digite o número que deseja para ser o exponente do cálculo exponêncial: '))
        print(f'O cálculo exponêncial tendo como base o  {t1} e como expoente o {t2} é {t1 ** t2}')

    print('''Você deseja fazer outro cálculo? 
[ 1 ] SIM
[ 2 ] NÃO''')
    outro = int(input('Digite 1 para SIM e 2 para NÃO: '))
    if outro == 1:

        escolha = 0
    else:
        print('OBRIGADO POR USAR NOSSA CALCULADORA, ATÉ A PRÓXIMA :)')
