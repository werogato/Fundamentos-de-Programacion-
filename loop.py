text = input('dame una palabra')
letra = "a"

for encontrar in text:
	if text.find(letra) != -1:
		print(f'la letra {letra} existe en la palabra')
	else:
		print(f'letra {letra} no existe en la palabra')

	break