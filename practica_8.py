lista = {
    1: {'peli': 'Cars', 'edad': "Todas las edades"},
    2: {'peli': 'El gato con botas', 'edad': "Todas las edades"},
    3: {'peli': 'Oppenheimer', 'edad': "Mayores de 18 años"},
}

print('Películas que desea ver:')
for num, peli in lista.items():
    print("{}. {}".format(num, peli['peli']))

x = int(input('Ingrese el número de la película: '))

pelicula = lista.get(x)
if pelicula:
    print('La película que seleccionó es "{}"'.format(
        pelicula['peli']), 'y su clasificacion es "{}"'.format(pelicula['edad']))
else:
    print("La película con ese número no está en la lista.")
