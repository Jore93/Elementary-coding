# -*- coding: utf-8 -*-

def laske_liike_energia(massa, nopeus):
    """Laskee kappaleen liike-energian annettujen massan ja nopeuden perusteella.""" 
    liike_energia = 0.5 * float(massa) * float(nopeus) ** 2
    return liike_energia
    