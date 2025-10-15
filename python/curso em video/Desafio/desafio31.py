print('---' *18)
print('              VALOR DE PASSAGEM')
print('---' *18)
dista = float(input('              Distancia percorrida:'))
if dista <= 200:
    valor = dista * 0.50
    print('O valor da sua passagem é R${:.2f}'.format(valor))
else:
    valor = dista * 0.45
    print('O valor da sua passagem é R${:.2f}'.format(valor))
