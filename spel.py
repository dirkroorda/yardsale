import collections
from random import seed, randrange
from utils import showDistribution


class Spel:
    """Code voor het spel

    We gebruiken de random generator van Python.
    Die genereert pseudo-random getallen, gebaseerd op een seed.

    Als we alvorens random getallen te genereren, de generator voorzien van
    een seed, dan zullen de gegenereerde getallen reproduceerbaar zijn.
    De volgende keer dat we de generator dezelfde seed geven, zal hij daarna
    precies dezelfde getallen genereren als in de vorige run.

    Als we het spel opzetten, dan doen geven we zo'n seed mee.
    Dat gebeurt in de methode `bigbang()`.
    We starten als het ware de wereld.

    Daarna kunnen we een spel beginnen, en rondes gaan doen.

    We kunnen ook weer nieuwe spelen beginnen, dan zetten we de bedragen voor de spelers
    en de bank weer op de beginwaarden. Maar we geven geen nieuw seed mee, dus
    het nieuwe spel zal anders verlopen dan het vorige spel.

    Een nieuw spel beginnen gebeurt met de methode `begin()`.
    """
    def __init__(self, nSpelers, startKapitaalSpeler, winstFactor, verliesFactor):
        self.nSpelers = nSpelers
        self.startKapitaalSpeler = startKapitaalSpeler
        self.startKapitaalBank = nSpelers * startKapitaalSpeler
        self.winstFactor = winstFactor
        self.verliesFactor = verliesFactor

        self.bigbang()
        self.bank = 0
        self.spelers = []
        self.nRonde = 0
        self.begin()

    def bigbang(self):
        seed(111111)

    def begin(self):
        nSpelers = self.nSpelers
        startKapitaalSpeler = self.startKapitaalSpeler
        startKapitaalBank = self.startKapitaalBank

        self.bank = startKapitaalBank
        self.spelers = [startKapitaalSpeler for n in range(nSpelers)]
        self.startSpelers = sum(self.spelers)
        self.nRonde = 0

    def ronde(self):
        nSpelers = self.nSpelers
        spelers = self.spelers
        winstFactor = self.winstFactor
        verliesFactor = self.verliesFactor

        for n in range(nSpelers):
            wv = randrange(0, 2)
            oud = spelers[n]
            nieuw = oud * (verliesFactor if wv == 0 else winstFactor)
            verschil = nieuw - oud
            self.bank -= verschil
            spelers[n] = nieuw
        self.nRonde += 1

    def rondes(self, aantalRondes, toonElke, opnieuw=False, verdeling=False):
        if opnieuw:
            self.begin()
        totaalRondes = 0
        while totaalRondes < aantalRondes:
            for ronde in range(toonElke):
                self.ronde()
                totaalRondes += 1
                if totaalRondes > aantalRondes:
                    break
            self.toon(verdeling=verdeling)

    def toon(self, verdeling=True):
        nRonde = self.nRonde
        spelers = self.spelers
        startSpelers = self.startSpelers
        bank = self.bank
        startKapitaalBank = self.startKapitaalBank

        data = collections.Counter()
        for huidig in spelers:
            data[huidig] += 1
        bankKapitaal = f"{int(round(100 * bank / startKapitaalBank)):>7}%"
        spelerKapitaal = f"{int(round(100 * sum(spelers) / startSpelers)):>7}%"
        print(
            f"Ronde {nRonde:>5}: bank ~ spelers {bankKapitaal} ~ {spelerKapitaal}"
        )
        if verdeling:
            showDistribution(data, "spelers", "bedrag")
