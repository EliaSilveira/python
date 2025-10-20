r1 = int(input('Digite a medida da primeira reta: '))
r2 = int(input('Digite a medida da segunda reta: '))
r3 = int(input('Digite a medida da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Temos um triangulo!')
else:
    print('As medidas fornecidas não resulta em um triangulo.')