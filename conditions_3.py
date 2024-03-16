cal = int(input('Dame tu calificacion entre 100 y 60\n'))

if cal >= 90:
    print('Tu calificacion es A')
elif cal >= 80:
    print ('Tu calificacion es B')
elif cal >= 70:
    print ('Tu calificacion es C')
elif cal >= 60:
    print ('Tu calificacion es D')
elif cal <= 50:
    print ('Tu calificacion es F')
else:
    print ('Tu calificacion no entra en el rango')