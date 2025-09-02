print('Calculando Dobro, triplo e Raiz Quadrada!!!')
n1 = int(input('Digite um numero: '))
dob = n1 * 2 #Dobro
trip = n1 * 3 #Multiplicação
raiz = n1 ** 0.5 #Para fazer a raiz quadrada
print('O numero é {}\n Dobro = {}\n Triplo = {}\n Raiz Quadrada {:.2f}'.format(n1, dob, trip, raiz))

print('---------------------------------------------------------------------------------------------------------')

n = int(input('Digite um numero: '))
print('O valor é {}, o Dobro {}, o triplo {} e a raiz quadrada é {:.2f}.'.format(n,(n*2), (n*3), (n**(1/2))))