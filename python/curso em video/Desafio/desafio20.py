from random import shuffle
#importação da biblioteca "RANDOM"
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
#Dar nomes aos alunos com as devidas variaveis a1,a2,a3 é a4
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de apresentação será: \n{}'.format(alunos))
#Escrever possivel lista de alunos para apresentação, de acordo com a lista que o usuario descrever acima.