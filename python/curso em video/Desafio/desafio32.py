print('    DECOBRINDO ANO BISSEXTO!')
print('===' * 16)
ano = int(input('Digite o ano:'))
biss = ano % 4
if biss == 0:
    print('Esse ano de {} é Bissexto!'.format(ano))
else:
    print('Esse ano de {} não é Bissexto!'.format(ano))