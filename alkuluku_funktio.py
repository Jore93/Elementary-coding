# -*- coding:UTF-8 -*-

def tarkista_alkuluku(luku):
    maxarvo = int(luku ** 0.5 + 1)
    if luku <= 1:
        print "Pieleen meni."
    for luvut in range(2, int(maxarvo)):
        if luku % luvut == 0:
            print "Kyseessä ei ole alkuluku."
            break
    else:
        print "Kyseessä on alkuluku."