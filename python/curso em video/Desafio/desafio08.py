print('======== CONVERSOR DE MEDIDA ========')
medida = float(input('Digite a medida que quer converter: '))
cent = medida * 100
milime = medida * 1000
quilo = medida / 1000
print('Mostre o valor em centimetro {:.0f}\n milimetro {:.0f} é\n Quilômetro {}'. format(cent, milime, quilo))