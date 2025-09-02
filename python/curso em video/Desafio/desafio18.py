from math import sin, radians, cos, tan
an = float(input('Digite o angulo: '))
seno = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print('Seno {:.2f}\n Cosseno {:.2f}\n tangente {:.2f}'.format(seno, coss, tang))
