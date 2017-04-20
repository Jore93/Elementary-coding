# -*- coding: utf-8 

hinta = int(raw_input("Anna hinta: "))
if hinta < 10:
    print "Ostan!"
elif hinta < 20:
    print "No ostetaan nyt."
elif hinta <= 50: 
    print "Kalliilla menee, mutta menkööt!"
else:
    print "Pidä tunkkis!"
