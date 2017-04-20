# -*- coding: UTF-8 -*-

luku1 = int(raw_input("Anna ensimmäinen luku: "))
luku2 = int(raw_input("Anna toinen luku: "))
maksimi = max(luku1, luku2)
minimi = min(luku1, luku2)
if luku1 == luku2:
    print "%s on %s:n tekijä." % (luku1, luku2)
elif luku1 != luku2:
    if luku1 > 0 and luku2 >0:
        if not maksimi % minimi != 0:
            print "%s on %s:n tekijä." % (minimi, maksimi)
        else:
            print "Kumpikaan luvuista ei ole toisen tekijä."
    elif luku1 < 0 and luku2 < 0:
        if not minimi % maksimi != 0:
            print "%s on %s:n tekijä." % (maksimi, minimi)
    elif maksimi > 0 and minimi < 0:
        if abs(maksimi) < abs(minimi):
            if not minimi %  maksimi != 0:
                print "%s on %s:n tekijä." % (maksimi, minimi)
        elif abs(maksimi) > abs(minimi) != 0:
            if not maksimi % minimi != 0:
                print "%s on %s:n tekijä." % (minimi, maksimi)
    elif not luku1 != 0 or not luku2 != 0:
        if not maksimi != 0:
            if not maksimi % minimi != 0:
                print "%s on %s:n tekijä." % (minimi, maksimi)
        elif not minimi != 0:
            if not minimi % maksimi != 0:
                print "%s on %s:n tekijä." % (maksimi, minimi)   