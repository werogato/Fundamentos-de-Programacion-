def operaciones(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div


resultado = operaciones(a=int(input('Primer digito\n')),
                        b=int(input('segundo digito\n')))
print('El resultado de la suma es: ', resultado[0])
print('El resultado de la resta es: ', resultado[1])
print('El resultado de la multiplicacion es: ', resultado[2])
print('El resultado de la division es: ', resultado[3])
