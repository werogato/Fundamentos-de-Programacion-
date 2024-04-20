
def fahrenheit_celsius():

    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5.0/9.0
    return print('{} Fahrengeit es igual a {} en Celcius'.format(fahrenheit, celsius))


def celsius_fahrenheit():

    celsius = int(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = 9.0/5.0 * celsius + 32
    return print('{} Celcius es igual a {} en Fahrenheit'.format(celsius, fahrenheit))


print('Convertidor de grados')


operacion = int(input(
    'Seleccione una operacion:\n [1]Fahrenheit a Celcius\n [2] Celcius a Fahrenheit\n'))

if operacion == 1:
    print(fahrenheit_celsius())
elif operacion == 2:
    print(celsius_fahrenheit())
