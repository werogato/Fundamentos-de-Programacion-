lista = ['casa', 'trigonometria avanzada', 'auto', 'garabato', 'concurrencia']

largo = 0
palabra_larga = None

for palabra in lista:
    if len(palabra) > largo:
        largo = len(palabra)
        palabra_larga = palabra


print('La palabra mas larga es', palabra_larga)
