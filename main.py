palos = ('copas', 'bastos', 'espadas', 'oros')
cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
baraja = []


def creaBaraja():
    baraja = []
    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return baraja


baraja1 = creaBaraja()
baraja2 = creaBaraja()

print(baraja1)
