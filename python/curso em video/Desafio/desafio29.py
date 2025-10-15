velo = float(input('RADAR CARRO:'))
if velo > 80:
    multa = (velo - 80) * 7
    print('R${:.2F}'.format(multa))
