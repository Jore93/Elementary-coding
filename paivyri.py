# -*- coding: UTF-8 -*-

paiva = raw_input("Anna lokakuun päivä: ")
paivat = ["tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai", "maanantai"]
if paiva.isdigit() and 1 <= int(paiva) <= 31:
    paiva = int(paiva)
    if not paiva % 7 != 0:
        print "Lokakuun %s. päivä vuonna 2013 on %s" % (paiva, paivat[6])
    if not paiva % 7 != 1 or paiva == 1:
        print "Lokakuun %s. päivä vuonna 2013 on %s." % (paiva, paivat[0])
    if not paiva % 7 != 2 or paiva == 2:
        print "Lokakuun %s. päivä vuonna 2013 on %s." % (paiva, paivat[1])
    if not paiva % 7 != 3 or paiva == 3:
        print "Lokakuun %s. päivä vuonna 2013 on %s." % (paiva, paivat[2])
    if not paiva % 7 != 4 or paiva == 4:
        print "Lokakuun %s. päivä vuonna 2013 on %s." % (paiva, paivat[3]) 
    if not paiva % 7 != 5 or paiva == 5:
        print "Lokakuun %s. päivä vuonna 2013 on %s." % (paiva, paivat[4])
    if not paiva % 6 != 6 or paiva == 6:
        print "Lokakuun %s. päivä vuonna 2013 on %s." % (paiva, paivat[5])   
else:
    print "Mikä tässä on nyt niin vaikeaa?"