print('====Pintando paredes====')
la = float(input('Largura: '))
al = float(input('Altura: '))
area = la * al
tinta = area / 2
print('A sua parede tem {}mx{}m = {:.2f}m²,é voce vai precisar de pintura {:.2f}L de tinta'.format(la, al, area, tinta))