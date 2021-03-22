pais = str(input('Digite o código do país com apenas dois dígitos (exemplo, Brasil é 55): '))
while pais.isdigit() == False:
    print('Gentileza, digite um código válido')
    pais = str(input('Digite o código do país: '))

ddd = str(input('Digite o ddd do estado com apenas dois dígitos (exemplo, Ceará é 85): '))
while ddd.isdigit() == False:
    print('Gentileza, digite um ddd válido')
    ddd = str(input('Digite o código do ddd: '))
telefone = str(input('Digite o número do telefone, apenas dígitos de 0 - 9: '))
while telefone.isdigit() == False:
    print('Gentileza, digite um telefone válido')
    telefone = str(input('Digite o número do telefone: '))

pais = int(pais)
ddd = int(ddd)
telefone = int(telefone)

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
