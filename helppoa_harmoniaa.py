# -*- coding:UTF-8 -*-

print "Syötä arvoja. Tyhjä syöte lopettaa."

luvut = []
while True:
    luku = raw_input("Anna luku: ")
    if not luku:
        break
    luvut.append(float(luku))

alku = 0        
for summa in luvut:
    alku = (alku + (1 / summa))
tulos = 1 / alku

print "Lukujen harmoninen keskiarvo on %.3f" % (tulos)