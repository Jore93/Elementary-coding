# -*- coding: utf-8 -*-

def tarkista_mittaukset(tulokset):
    for arvo in tulokset[:]: 
        if arvo > 1000:
            tulokset.remove(arvo)
        
    while len(tulokset) < 5:
        tulokset.append(tulokset[-1])

testivektori = [20.45, 6452.0, 30.12, 2347.15]
tarkista_mittaukset(testivektori)
for arvo in testivektori:
    print "%.2f" % (arvo)