print('DESAFIO DO SALARIO')
salario = float(input('Qual o seu salario? '))
if salario <= 1250:
    novosal = salario + (salario * 15 / 100)
else:
    novosal = salario + (salario * 10 /100)
print('Seu salario de \033[1;31mR${:.2f}\033[m aumento para \033[32mR${:.2f}\033[m agora.'.format(salario,novosal))
