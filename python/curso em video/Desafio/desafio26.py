frase = str(input('Digite uma frase: ')).upper().strip()
print('A Letra A apareceu {} vezes na frase'.format(frase.count('A')))
#USAR ESSE METODO PARA CONTAR QUANTOS "a" TINHA NA FRASE
print('A letra aparece na primeira vez {}'.format(frase.find('A')+1))
#Vai aparecer a primeira posição da letra A
print('A ultima posição do A é: {}'.format(frase.rfind('A')+1))
#vai aparecer a posição do Ultimo A



