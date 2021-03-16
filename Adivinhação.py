from random import randint
from time import sleep

computador = randint(1, 100)

print('-=' * 10, 'BEM VINDO AO JOGO DE ADIVINHAÇÃO DO SADN0X', '=-' * 10)
sleep(2)
print('''O jogo consiste no seguinte, o computador irá escolher um número de 1 a 100
e você deve adivinhar que número é esse. O número de tentativas será de acordo com a 
dificuldade escolhida, entre fácil, intermediário e difícil. VAMOS LÁ?!?!

ESCOLHA A DIFICULDADE:
[ 1 ] FÁCIL
[ 2 ] INTERMEDIÁRIO
[ 3 ] DIFÍCIL''')

dificuldade = int(input('Digite a dificuldade escolhida: '))

while dificuldade < 1 or dificuldade > 3:
    print('OPÇÃO INCORRETA, VAMOS TENTAR NOVAMENTE.')
    print('Digite a dificuldade escolhida[ 1 - 3 ]: ')

if dificuldade == 1: #DIFICULDADE FÁCIL, 10 TENTATIVAS
    tentativas = 10
    while tentativas > 0:
        print(f'Você escolheu a dificuldade FÁCIL, você tem {tentativas} TENTATIVAS de concluir o jogo.')
        sleep(1)
        num = int(input('Digite o número escolhido: '))
        sleep(1)
        if num > computador:
            print('O número escolhido foi maior que o do computador.')
            tentativas -= 1
        if num < computador:
            print('O número escolhido foi menor que o do computador.')
            tentativas -= 1
        if num == computador:
            print('VOCÊ VENCEU, MUITO BEM!!!!!!!!!!')
            break
        if tentativas == 0:
            print('VOCÊ PERDEU, VAMOS JOGAR NOVAMENTE OUTRA HORA!')

if dificuldade == 2:  # DIFICULDADE INTERMEDIÁRIA, 5 TENTATIVAS
    tentativas = 5
    while tentativas > 0:
        print(f'Você escolheu a dificuldade INTERMEDIÁRIA, você tem {tentativas} TENTATIVAS de concluir o jogo.')
        sleep(1)
        num = int(input('Digite o número escolhido: '))
        sleep(1)
        if num > computador:
            print('O número escolhido foi maior que o do computador.')
            tentativas -= 1
        if num < computador:
            print('O número escolhido foi menor que o do computador.')
            tentativas -= 1
        if num == computador:
            print('VOCÊ VENCEU, MUITO BEM!!!!!!!!!!')
            break
        if tentativas == 0:
            print('VOCÊ PERDEU, VAMOS JOGAR NOVAMENTE OUTRA HORA!')

if dificuldade == 3:  # DIFICULDADE DIFÍCIL, 3 TENTATIVAS
    tentativas = 3
    while tentativas > 0:
        print(f'Você escolheu a dificuldade DIFÍCIL, você tem {tentativas} TENTATIVAS de concluir o jogo.')
        sleep(1)
        num = int(input('Digite o número escolhido: '))
        sleep(1)
        if num > computador:
            print('O número escolhido foi maior que o do computador.')
            tentativas -= 1
        if num < computador:
            print('O número escolhido foi menor que o do computador.')
            tentativas -= 1
        if num == computador:
            print('VOCÊ VENCEU, MUITO BEM!!!!!!!!!!')
            break
        if tentativas == 0:
            print('VOCÊ PERDEU, VAMOS JOGAR NOVAMENTE OUTRA HORA!')
    print('FIM DE JOGO!')
