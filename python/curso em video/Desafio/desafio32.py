from datetime import date
print('===' * 16)
print('    DECOBRINDO SE ANO É BISSEXTO!')
print('===' * 16)
ano = int(input('Digite o ano ou coloque 0 para o ano atual: '))
biss = ano % 4
if ano == 0:
    ano = date.today().year
if biss == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano de {} é Bissexto!'.format(ano))
else:
    print('Esse ano de {} não é Bissexto!'.format(ano))