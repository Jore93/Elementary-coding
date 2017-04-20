# -*- coding: utf-8 -*-

def laske_keskiarvo(alkiot):
    """Laskee annettujen energioiden keskiarvon."""
    keskiarvo = float(sum(alkiot)) / len(alkiot)
    return keskiarvo
    
print laske_keskiarvo(alkiot=(1, 2, 3))
print laske_keskiarvo(alkiot=[0, 0, 0, 1, 0, 0, 0])
print laske_keskiarvo(alkiot=(0.5, 1.0, 1.5, 2.0))