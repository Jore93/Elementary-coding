# -*- coding:UTF-8 -*-

while True:
    pelaaja_1 = raw_input("Pelaaja 1, anna arvattava sana: ").lower()
    if len(pelaaja_1) < 2:
        print "Liian lyhyt sana, senkin tohelo!"
    else:
        break
        
while True:
    pelaaja_2 = raw_input("Pelaaja 2, anna arvauksesi: ").lower()
    if len(pelaaja_2) == 1:
        luku = 0
        for merkki in pelaaja_1:
            if merkki == pelaaja_2:
                luku = luku + 1
        print "Arvattavassa sanassa on %d %s-merkki(ä)." % (luku, pelaaja_2)
    else:
        if pelaaja_2 == pelaaja_1:
            print "Oikein! Hurraa!"
            break
        else:
            print "Pieleen meni!"   