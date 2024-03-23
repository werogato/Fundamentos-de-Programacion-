text = input('dame una palabra: ')
letra = 'a'
tiene_letra = False

for letra_actual in text:
    if letra_actual == letra:
        tiene_letra = True

if tiene_letra:
    print('La palabra tiene la letra "a"')
else:
    print('La palabra no tiene la letra "a"')