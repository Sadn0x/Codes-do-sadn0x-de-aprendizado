pais = int(input('Digite o código do país com apenas dois dígitos (exemplo, Brasil é 55): '))
ddd = int(input('Digite o ddd do estado com apenas dois dígitos (exemplo, Ceará é 85): '))
telefone = int(input('Digite o número do telefone, apenas dígitos de 0 - 9: '))
pais *= 100000000000
ddd *= 1000000000
if telefone < 900000000:
    telefone += 900000000
telefone += pais
telefone += ddd

mensagem = str(input('Digite sua mensagem: ')).split()
texto = '%20'.join(mensagem)

print('o seu link de whatsapp personalizado é: ')
print(f'https://api.whatsapp.com/send?phone={telefone}&text={texto}')
