print('   VERIFICANDO O MAIOR E O MENOR NUMERO COM IF E ELSE')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
# VERIFICANDO O MAIOR NUMERO
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

# VERIFICANDO O MENOR NUMERO
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

print('O Maior numero é {}'.format(maior))
print('O Menor numero é {}'.format(menor))