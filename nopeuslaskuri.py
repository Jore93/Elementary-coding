#-*- coding: UTF-8 -*-
matka = raw_input("Anna auton kulkema matka (m): ")
matka = float(matka)
aika = raw_input("Anna matkaan kulunut aika (s): ")
aika = float(aika)
nopeus = float(matka / aika) * 3.6
lause = "%.2f metriä %.2f sekunnissa kulkeneen auton nopeus on %.2f km/h." % (matka, aika, nopeus)
print lause