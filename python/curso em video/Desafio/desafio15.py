distancia = float(input('Quantos Km voce andou?'))
dia = int(input("Quantos dias com o carro ficou? "))
pago = (dia * 60) + (distancia * 0.15)
print("Você andou {:.2f}Km e ficou {} dias com o carro, o total a pagar é R${:.2f}".format(distancia, dia, pago))

