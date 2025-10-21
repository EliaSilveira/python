from time import sleep
print('---' *18)
print(' VALOR DE PASSAGEM')
print('---' *18)
dista = float(input(' Distancia percorrida:'))
print('\033[4;36mVerificando distancia e valores, só um momento\033[m')
print('\033[4;36mAguarde!!!\033[m')
sleep(5)
print('Você está para fazer um viagem de {}km'.format(dista))
if dista <= 200:
    valor = dista * 0.50
else:
    valor = dista * 0.45
print('O valor da sua passagem é \033[1;32mR${:.2f}\033[m'.format(valor))
