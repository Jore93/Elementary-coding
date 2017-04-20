# -*- coding: utf-8 -*-

print "Fibonaccin lukujono alkaa luvuilla 0 ja 1."
luku = [0, 1]
toisto = int(raw_input("Montako lukua generoidaan lisää? "))
if toisto > 1:
    print luku[1]
    lukujono = luku[1] + luku[1]
    luku.append(lukujono)
    print lukujono
    for lukujono in range(toisto - 2):
        lukujono = luku[-1] + luku[-2]
        luku.append(lukujono)
        print lukujono