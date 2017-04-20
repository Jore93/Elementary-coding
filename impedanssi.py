# -*- coding: UTF-8 -*-
 
pi = 3.142
komponentin_tyyppi = raw_input("Anna komponentin tyyppi (R, L, C): ").upper()
if komponentin_tyyppi == "R" or "L" or "C":
    if komponentin_tyyppi == "R":
        vastuksen_arvo = float(raw_input("Anna komponentin arvo: "))
        print "Vastuksen impedanssi on %.2f ohmia." % (vastuksen_arvo)
    elif komponentin_tyyppi == "L":
        L = float(raw_input("Anna komponentin arvo: "))
        f_kela = float(raw_input("Anna komponentin taajuus: "))
        kelan_impedanssi = float(2 * pi * f_kela * L)
        print "Kelan impedanssi taajuudella %.2f Hz on %.2f ohmia." % (f_kela, kelan_impedanssi)
    elif komponentin_tyyppi == "C":
        C = float(raw_input("Anna komponentin arvo: "))
        f_kondensaattori = float(raw_input("Anna komponentin taajuus: "))
        kondensaattorin_impedanssi = float(1 / (2 * pi * f_kondensaattori * C))
        print "Kondensaattorin impedanssi taajuudella %.2f Hz on %.2f ohmia." % (f_kondensaattori, kondensaattorin_impedanssi)
    else:
        if not komponentin_tyyppi == "R" or "L" or "C":
            print "Sallittuja komponentteja ovat R, L ja C!"