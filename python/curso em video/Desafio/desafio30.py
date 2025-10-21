print('==' * 16)
print(' PAR OU IMPAR')
print('==' * 16)
print('VAMOS DESCOBRIR SE O NUMERO É PAR OU IMPAR!')
num = int(input('Digite um numero: '))
num2 = num % 2
if num2 == 0:
    print('{}, esse numero é \033[34mPAR'.format(num))
else:
    print('{}, esse numero e \033[33mIMPAR'.format(num))
