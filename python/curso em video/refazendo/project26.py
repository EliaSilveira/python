frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A posição que a primeira aparece é {}'.format(frase.find('A')+1))
print('A Ultima vez que o A aparece é {}'.format(frase.rfind('A')+1))

