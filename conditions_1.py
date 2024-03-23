
num1 = input(print('Dame tu primer digito'))
num2 = input(print('Dame tu segundo digito'))

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num2 > num1:
    print(f'{num2} es mayor que {num1}')
else:
    print("ambos numeros son iguales")