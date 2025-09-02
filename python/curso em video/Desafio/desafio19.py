from random import choice
a1 = str(input('Nome do aluno: '))
a2 = str(input('Nome do aluno: '))
a3 = str(input('Nome do aluno: '))
a4 = str(input('Nome do aluno: '))
#Variaveis para 4 alunos
alunos = [a1, a2, a3, a4]
#acima realizado a lista
print('Os alunos selecionados foram: {}'.format(alunos))
#mostra a lista do alunos devimente selecionados
print('O alunos selecionado desta lista foi: {}'.format(choice(alunos)))
#aqui a importação "choice" faz o sorteo da lista de alunos
