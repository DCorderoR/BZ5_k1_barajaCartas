import cartas

b = cartas.creaBaraja()
manos = cartas.repartir(b, 3, 5)

print(manos)