import random

num_secret = random.randint(0, 10)

num_usuario = int(input('Ingresa un numero\n'))

while num_usuario != num_secret:
    num_usuario = int(input('sigue intentando, ingresa otro\n'))
if num_usuario == num_secret:
    print('felicidades, haz ganado un cupon')
