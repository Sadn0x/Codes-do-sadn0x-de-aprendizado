from random import randint

print('-=' * 15)
print('Vamos jogar PAR ou IMPAR')
print('-=' * 15)

cont = 0
repetir = 1

while repetir == 1:
    computador = randint(0, 10)
    pi = str(input('Você deseja ser PAR ou IMPAR[P/I]? ')).upper().strip()[0]
    while pi not in 'PI':
        print('Digite um valor válido: ')
        pi = str(input('Você quer ser PAR ou IMPAR[P/I]? ')).upper().strip()[0]
    if pi in 'I':
        print('Você escolheu IMPAR.')
    elif pi in 'P':
        print('Você escolheu PAR.')
    jogador = int(input('Digite um valor(se desejar encerrar, digite 999): '))
    resultado = computador + jogador
    if resultado > 1000:
        print('JOGO ENCERRADO PELO JOGADOR.')
        break
    if pi in 'I':
        if resultado % 2 != 0:
            print(f'O resultado deu {resultado}, que é impar, o jogador venceu!')
            cont += 1
        if resultado % 2 == 0:
            print(f'O resultado deu {resultado}, que e é par, o jogador perdeu!')
            repetir = 0
            break
    if pi in 'P':
        if resultado % 2 == 0:
            print(f'O resultado deu {resultado}, que é par, o jogador venceu!')
            cont += 1
        if resultado % 2 != 0:
            print(f'O resultado deu {resultado}, que e é impar, o jogador perdeu!')
            repetir = 0
            break
print(f'O jogador venceu {cont}x.')
