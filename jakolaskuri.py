# -*- coding: UTF-8 -*-
 
jaettava = raw_input("Anna jaettava: ")
if not jaettava.isdigit():
    print "Jaettava ei ole positiivinen kokonaisluku eikä nolla!"
else:
    jakaja = raw_input("Anna jakaja: ")
    if jakaja < "0":
        print "Jakaja ei ole positiivinen kokonaisluku!"
    elif not jakaja != "0":
        print "Nollalla ei voi jakaa!"
    else: 
        jaettava.isdigit() and jakaja.isdigit()
        osamaara = int(abs(int(jaettava)) / abs(int(jakaja)))
        print "Osamäärä: %s" % osamaara