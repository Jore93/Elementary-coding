# -*- coding:UTF-8 -*-

import math
import sys

def laske_desibelit(mitattu_teho, vertailuteho):
    """Laskee, paljonko mitattu teho on desibeleinä tietyllä vertailutasolla."""
    desibelit = float(10 * math.log10(mitattu_teho / vertailuteho))
    return desibelit
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            mitattu_teho = float(sys.argv[1])
            vertailuteho = float(sys.argv[2])
            desibelit = laske_desibelit(mitattu_teho, vertailuteho)
            print "%.2f W:n teho %.2f W:n vertailutasolla on %.2f desibeliä." % (mitattu_teho, vertailuteho, desibelit)
        except (ValueError, ZeroDivisionError):
            print "Tehon ja vertailutason on oltava positiivisia lukuja!"                
    else:
        print "Väärä määrä komentoriviargumentteja!"