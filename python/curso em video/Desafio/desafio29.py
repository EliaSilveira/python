print('-++-' * 20)
print('RADAR ELETRONICO')
print('-++-' * 20)
velocidade = float(input('Velocidade do Carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi \033[1:31mmultado R${:.2F}\033[m, dirija com resposabilidade.'.format(multa))
print('Tenha um ótimo dia e mantenha o respeito no trasinto!')