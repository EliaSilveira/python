import random
sort = int(input('Digite um numero: '))
num = random.randint(1, 5)
print(num)
if sort == num:
    print('Voce Acertou o numero Sorteado!')
else:
    print('ERROU')