total_preguntas = int(input('Total de preguntas\n'))
can_correctas = int(input('Total de aciertos\n'))

calificacion = (can_correctas / total_preguntas)*100

print('Tu calificacion es:', "{0:.2f}".format(
    calificacion), 'y tuviste', total_preguntas - can_correctas, 'incorrectas')
