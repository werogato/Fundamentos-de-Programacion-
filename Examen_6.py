lista = [1, 2, 4]


num = int(input('Introduzca el numero que quiere buscar'))

try:
    if lista.index(num) or lista.index(num) == 0:

        print('El numero se encuentra en la posicion:{}'.format(lista.index(num)))
        x = int(input('Desea borrar el numero?\n [1]si  [2]no\n'))
        if x == 1:
            lista.remove(num)
            print('elemento removido:\n', lista)
        else:
            print('tenga buen dia')
            exit

except ValueError:
    x = int(
        input('El numero no se encuentra, desea añadirllo?\n [1]si  [2]no\n'))

    if x == 1:
        lista.append(num)
        print('numero añadido a la lista:\n', lista)

    else:
        print('tenga buen dia')
        exit
