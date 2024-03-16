num1 = int (input('Dame tu primer digito\n'))
num2 = int (input('Dame tu segundo digito\n'))

def sum(num1, num2):
    return num1 + num2

resultado_sum = sum(num1, num2)

def res(num1, num2):
    return num1 - num2

resultado_res = res(num1, num2)

def mul(num1, num2):
    return num1 * num2

resultado_mul = mul(num1, num2)

def div(num1, num2):
    return num1 / num2

resultado_div = div(num1, num2)

def mod(num1, num2):
    return num1 % num2

resultado_mod = mod(num1, num2)

def exp(num1, num2):
    return num1 ** num2

resultado_exp = exp(num1, num2)

print (f'El resultado de la suma es: {resultado_sum}')
print (f'El resultado de la resta es: {resultado_res}')
print (f'El resultado de la mul es: {resultado_mul}')
print (f'El resultado de la div es: {resultado_div}')
print (f'El residuo la div es: {resultado_mod}')
print (f'El resultado de la exp es: {resultado_exp}')