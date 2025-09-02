nome = input('Digite o seu nome completo:')
print('Seu nome em MAIUSCULO: {}'.format(nome.upper()))
#Para deixar todas as letras MAIUSCULA

print('Seu em minusculo: {}'.format(nome.lower()))
#Para deixar todas as letras minusculas

print('Seu nome tem a quantidade de: {} letras'.format(len(nome) - nome.count(' ')))
# Para Fazer a contagem de letras sem o espaço entre as palavras

print('Seu primeiro nome tem: {} letras'.format(len(nome.split()[0])))
#faz a contagem do primeiro nome que aparece