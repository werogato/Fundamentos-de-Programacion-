print('Calcular Indice de masa corporal\n')

kg = float(input('Dame tu peso\n'))
alt = float(input('Dame tu altura\n'))

indice_masa = kg / (alt)**2

print('Su indice de masa corporal es:', "{0:.2f}".format(indice_masa))
