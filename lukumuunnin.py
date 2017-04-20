# -*- coding:UTF-8 -*-

lista = []
arvo = raw_input("Anna muutettava arvo: ")
lista = lista.append(arvo)
liite = ["a", "j", "p", "n", "u", "m", "K", "M", "G", "T"]
kerroin = ["e-18", "e-15", "e-12", "e-9", "e-6", "e-3", "e+3", "e+6", "e+9", "e+12"]
if arvo[-1] in liite:
    paikka = liite.index(arvo[-1])
    #liitteessä kirjaimen paikka sijoitetaan kerroin listaan paikkaan
    print arvo[0:-1] + kerroin[int(paikka)]
else:    
    print round(float(arvo), 1)