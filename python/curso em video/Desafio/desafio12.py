preço = float(input('Valor R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto, agora custa R${:.2f}'.format(preço, novo))