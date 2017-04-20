# -*- coding:UTF-8 -*-

import math
import cmath
import sys

def muunna_napakoordinaateiksi(kompleksiluku):
    """Muuntaa annetun kompleksiluvun napakoordinaattimuotoon."""
    napakoordinaatti = cmath.polar(kompleksiluku)
    kiertokulma = math.degrees(napakoordinaatti[1])
    koordinaatti = (napakoordinaatti[0], kiertokulma)
    return koordinaatti
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        kompleksiluku = complex(sys.argv[1])
        koordinaatit = muunna_napakoordinaateiksi(kompleksiluku)
        print "%.4f < %.2f°" % (koordinaatit[0], koordinaatit[1])  
    else:
        print "Väärä määrä komentoriviargumentteja!"    