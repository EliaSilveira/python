nome = str(input('Digite o seu nome inteiro: ')).strip()
prime = nome.split()[0]
#Para conseguir localizar o primeiro nome, ele separa a cadeia de caracteriz atraves do '0'
segun = nome.split()[-1]
# Com o [-1] ele pega a ultima palavra descrita
print('Prazer! Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(prime))
print('Seu ultimo sobrenome é: {}'.format(segun))


