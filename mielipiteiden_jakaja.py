#-*- coding: UTF-8 -*-

mielipide1 = raw_input("Syötä ensimmäinen mielipide: ")
lkm_mielipide1 = float(raw_input("Syötä ensimmäisen mielipiteen kannatusluku: "))
mielipide2 = raw_input("Syötä toinen mielipide: ")
lkm_mielipide2 = float(raw_input("Syötä toisen mielipiteen kannatusluku:"))

print " "
print "Tulokset (%):"
print ""

lkm_koko = float(lkm_mielipide1 + lkm_mielipide2)
osuus_mielipide1 = (lkm_mielipide1 / lkm_koko) * 100
osuus_mielipide2 = (lkm_mielipide2 / lkm_koko) * 100
vali1 = max(len(mielipide1), len(mielipide2))
valimerkki = "*"
vali = " "
palkki1 = valimerkki * int(round(50 * osuus_mielipide1 / 100))
palkki2 = valimerkki * int(round(50 * osuus_mielipide2 / 100))
vali2 = 50

print "%s" % mielipide1.capitalize().ljust(vali1), palkki1.ljust(vali2), "%.1f" % osuus_mielipide1   
print "%s" % mielipide2.capitalize().ljust(vali1), palkki2.ljust(vali2), "%.1f" % osuus_mielipide2 