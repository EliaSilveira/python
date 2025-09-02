print('==== CONVERSOR DE MOEDAS ====')
real = float(input('Dinheiro na carteira? R$'))
iene = real / 0.038
euro = real / 6.39
dolar = real / 3.27
print('Com R${} reias você possui US${:.2f} dolares'.format(real, dolar))
print('euro {:.2f}, iene {:.2f}'.format(euro, iene))




