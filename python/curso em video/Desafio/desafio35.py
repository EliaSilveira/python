print('-++-' * 20)
print('DESAFIO DO TRIANGULO')
print('-++-' * 20)
r1 = int(input('Digite a medida da primeira reta: '))
r2 = int(input('Digite a medida da segunda reta: '))
r3 = int(input('Digite a medida da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #PARA VERIFICAR AS MEDIDAS FORMAM UM TRIANGULO
    print('Temos um TRIANGULO!')
else:
    print('As medidas fornecidas NÃO RESULTA em um TRIANGULO.')