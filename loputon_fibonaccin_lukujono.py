# -*- coding: utf-8 -*-

import datetime

luku = [0, 1]
aika1 = datetime.datetime.now()
while True:
    try:
        lukujono = luku[-1] + luku[-2]
        luku.append(lukujono)
    except KeyboardInterrupt:
        aika2 = datetime.datetime.now()
        lukujen_lkm = int(len(luku))
        kulunut_aika = aika2 - aika1
        print "Laskettiin %s uutta Fibonaccin lukua ajassa %s." % (lukujen_lkm, kulunut_aika)
        break