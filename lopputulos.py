# -*- coding: UTF-8 -*-

lopputulos = raw_input("Anna ottelun lopputulos: ")
merkki = "-"
paikka = lopputulos.find(merkki)
luku_1 = lopputulos[0:paikka]
luku_2 = lopputulos[paikka:]
maaliero = int(luku_1) + int(luku_2)
print "Joukkueiden välinen maaliero on", str(maaliero)