import random

num_1 = random.randint(0, 10)
vidas = 1

try:
    num_usuario = int(input('ingresa un numero'))
except ValueError:
    print('solo se aceptan numeros')
else:

    if num_usuario >= 0:

        
            while num_usuario != num_1 and vidas < 3:
                vidas = vidas + 1
                if num_usuario < num_1:
                    num_usuario = int(input('es un numero mas grande'))
                elif num_usuario > num_1:
                    num_usuario = int(input('es un numero mas chico'))

            if num_usuario == num_1:
                print ('adivinaste')

            if num_usuario != num_1:
                print ('fallaste')


    else:
        print('no se aceptan numeros negativos')

