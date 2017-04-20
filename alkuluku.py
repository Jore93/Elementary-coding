# -*- coding:UTF-8 -*-

syote = raw_input("Anna kokonaisluku, joka on suurempi kuin 1: ")
luku = int(syote)

if luku > 1:
    alkuluvut = []
    for alkuluku in range(2, int((luku ** 0.5) + 1)):
        jakojaannos = luku % alkuluku
        alkuluvut.append(jakojaannos)
    
    if 0 in alkuluvut[:]:
        print "Kyseessä ei ole alkuluku."
    else: 
        print "Kyseessä on alkuluku."      

else:        
    print "Pieleen meni."    