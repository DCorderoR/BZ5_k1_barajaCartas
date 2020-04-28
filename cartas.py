import random


class Baraja():
    palos = ('copas', 'bastos', 'espadas', 'oros')
    cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')

    def __init__(self):
        self.__creaBaraja()

    def __creaBaraja(self):
        self.naipes = []
        self.mano = []
        for palo in self.palos:
            for carta in self.cartas:
                naipe = carta + palo
                self.naipes.append(naipe)

    def mezclar(self):
        br = []
        while len(self.naipes) != len(br):
            n = random.randint(0, len(self.naipes)-1)
            while self.naipes[n] in br:
                n = random.randint(0, len(self.naipes)-1)
            br.append(self.naipes[n])
        self.naipes[:] = br

    def repartir(self, players, cards):
        for p in range(players):
            self.mano.append([])

        for ic in range(cards):
            for ij in range(players):
                carta = self.naipes.pop(0)
                self.mano[ij].append(carta)

    def invertir(self):
        for i in range(len(self.naipes)//2):
            aux = self.naipes[i]
            self.naipes[i] = self.naipes[-1-i]
            self.naipes[-1-i] = aux

    def recoger(self):
        self.__creaBaraja()


if __name__ == '__main__':
    b = Baraja()
    b.mezclar()
