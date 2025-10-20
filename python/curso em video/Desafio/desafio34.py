print('DESAFIO DO SALARIO')
salario = float(input('Qual o seu salario? '))
if salario <= 1250:
    novosal = salario + (salario * 15 / 100)
else:
    novosal = salario + (salario * 10 /100)
print('Seu novo Salario é R${:.2f}'.format(novosal))
