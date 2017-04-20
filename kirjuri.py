# -*- coding:UTF-8 -*-

import sys
 
def kirjoita_tiedostoon(filunimi, sisalto):
    """Kirjoittaa annetun sisällön määrätyn nimiseen tiedostoon ja sulkee tiedoston."""
    tiedosto = open(filunimi, "a")
    tiedosto.write(("%s") % str(sisalto))
    tiedosto.close()
       
if __name__ == "__main__":
    arvostelu = "Arvosanat:\n"
    try:
        tiedostonimi = sys.argv[1]
    except IndexError:
        print "Virhe: kohdetiedoston nimi on annettava komentoriviargumenttina!"
        sys.exit()
    while True:
        nimi = str(raw_input("Anna opiskelijan nimi tai lopeta antamalla q: "))
        if nimi == "q":
            if arvostelu == "Arvosanat:\n":
                print "Et antanut yhtään arvosanaa, joten tiedostoa ei kirjoitettu!"
                sys.exit()
            else:
                print "Kirjoitettiin arvosanat tiedostoon %s." % tiedostonimi
                kirjoita_tiedostoon(sys.argv[1], arvostelu)
                break
        else:
            try:
                arvosana = int(raw_input("Anna opiskelijan arvosana: "))
            except ValueError:
                print "Virhe: arvosanan on oltava kokonaisluku!"
                continue
            rivi = "\n%s: %s" % (nimi, str(arvosana))
            arvostelu = arvostelu + rivi