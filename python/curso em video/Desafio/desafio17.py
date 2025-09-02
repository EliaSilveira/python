from math import sqrt, hypot

cateto_a = float(input('Digite um valor: '))
cateto_b = float(input('Digite um valor :'))

hipotenusa = sqrt(cateto_a**2 + cateto_b**2)
print('A sua Hipotenusa é {:.2f}'.format(hipotenusa))



cateto_a = float(input('Digite um valor: '))
cateto_b = float(input('Digite um valor :'))
#hypot = calculo da hipotenusa
hi = hypot(cateto_a, cateto_b)
print('A sua Hipotenusa é {:.2f}'.format(hi))
