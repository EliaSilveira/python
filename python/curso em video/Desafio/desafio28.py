import random
from time import sleep
print('<==>' * 20)
print('**** JOGO ADIVINHE UM NUMERO DE 1 A 5 E TENTE GANHAR DA MAQUINA  ****')
print('<==>' * 20)
jogador = int(input('Por favor, digite um numero: '))
print('\033[4;35mPROCESSANDO....\033[m')
sleep(3)
num = random.randint(1, 5)# FAZ O PC SORTEAR O NUMERO
print(num)
if jogador == num:
    print('Parabéns, você \033[4;33mACERTOU\033[m o numero sorteado!')
else:
    print('Que pena mas você \033[1;31;40mERROU!!!\033[m')