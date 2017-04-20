# -*- coding: utf-8 -*-
import sys
 
def lue_tiedosto(tnimi):
    """Avaa tiedoston, lukee sen sisällön ja sulkee sen. Tiedoston sisältö palautetaan merkkijonona."""
    tiedosto = open(tnimi)
    teksti = tiedosto.read()
    tiedosto.close()
    return teksti   
       
if __name__ == "__main__":
    try:
        print lue_tiedosto(sys.argv[1])
    except IndexError:
        print "Virhe: tiedoston nimi on annettava komentoriviargumenttina!"
        sys.exit()
    except IOError:
        print "Virhe: tiedostoa %s ei löytynyt!" % sys.argv[1]
        sys.exit()