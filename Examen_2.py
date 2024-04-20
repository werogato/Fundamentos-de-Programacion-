num = int(input('Dame un rango\n'))

for numeros in range(num):

    if numeros % 2 == 0:
        print(f'{numeros} es par')
    else:
        print(f'{numeros} es impar')
