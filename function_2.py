number_1 = int (input('Dame tu primer digito\n'))
number_2 = int (input('Dame tu segundo digito\n'))
operacion = int (input('Selecciona tu operacion\n 1.Suma 2.Resta 3.Division 4.Multiplicacion 5.Exponente \n'))


def operaciones(num1, num2, operacion):
    if operacion == 1:
       return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 / num2
    elif operacion == 4:
        return num1 * num2
    elif operacion == 5:
        return num1 ** num2
    else:
        print ('operacion invalida')

result = operaciones(number_1, number_2, operacion)
print(f'el resultado de tu operacion es: {result}')