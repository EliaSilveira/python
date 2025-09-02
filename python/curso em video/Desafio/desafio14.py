temp = float(input('Graus celcius para fahrenheit? '))
far = (temp * 9/5) + 32
print('Temperatura {:.1f}°F'.format(far))

temper = float(input('Graus de Fahrenheit para celcius: '))
cel = (temper - 32) * 5/9
print('Temperatura {:.1f}° C'.format(cel))