import matplotlib.pyplot as plt
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas = [148969,167844, 189830, 211905, 188108, 204949, 239139, 234982, 235399, 261515, 248069, 236174]
plt.plot(meses, vendas, color='blue', linewidth=2)
plt.title('Vendas de Carros Ano de 2024')
plt.xlabel('Meses')
plt.ylabel('Venda(R$)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
