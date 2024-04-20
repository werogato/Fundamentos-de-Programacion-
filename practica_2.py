numero = int(input("Cantidad de materias: "))
cal = []
for i in range(numero):
    cal.append(float(input("Materia %s : " % (i+1))))
if numero == len(cal):
    promedio = sum(cal) / len(cal)

print(promedio)
