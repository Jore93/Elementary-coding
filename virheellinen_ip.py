# -*- coding:UTF-8 -*-

def tarkista_ip(ip):
    """Tarkistaa. onko merkkijonona annettu IPv4-osoite oikeaa muotoa."""
    ip = ip.split(".")
    if len(ip) != 4:
        return False
    for byte in ip:
        if not byte.isdigit() or int(byte) < 0 or int(byte) > 255:
            return False
    else:
        return True
        
def etsi_virheellinen_ip(osoitteet):
    """Palauttaa annetuista IPv4-osoitteista ensimmäisen virheellisen."""
    return next(ip for ip in osoitteet if not tarkista_ip(ip))


import osoitteet
tuloste = osoitteet.hae_osoitteet()
try:
    virhe = etsi_virheellinen_ip(tuloste)
except StopIteration:
    print "Kaikki osoitteet olivat oikeaa muotoa."
else:
    print "Virheellinen IP: %s." % (virhe)