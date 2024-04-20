import random

aleatorio = random.randint(1, 100)

print('Adivina el numero entre 1y 100')

for advinar in range(5):

    x = int(input('Ingresa un numero\n'))

    if aleatorio == x:
        print('adivinaste')
        break
    else:
        print('sigue intentando\n')
else:
    print('suerte para la proxima')
