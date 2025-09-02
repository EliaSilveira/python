salario = float(input("Salario: "))
novosal = salario + (salario * 15 / 100)# formula de porcetagem
print('Se salario com um aumento de 15% ficou R${:.2f}'.format(novosal))