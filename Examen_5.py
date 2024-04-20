def suma(a, b):
    suma = a + b
    return print(suma)


def resta(a, b):
    resta = a - b
    return print(resta)


def mult(a, b):
    mult = a * b
    return print(mult)


def div(a, b):
    div = a / b
    return print(div)


def modulo(a, b):
    por = a % b
    return print(por)


def exp(a, b):
    exp = a ** b
    return print(exp)


print('seleccione una operacion\n')
print('[1]suma [2]resta [3]multiplicacion [4]division [5]Modulo [6]exponente')
operacion = int(input())
a = int(input('primer digito\n'))
b = int(input('segundo digito\n'))
if operacion == 1:
    suma(a, b)
elif operacion == 2:
    resta(a, b)
elif operacion == 3:
    mult(a, b)
elif operacion == 4:
    div(a, b)
elif operacion == 5:
    modulo(a, b)
elif operacion == 6:
    exp(a, b)
