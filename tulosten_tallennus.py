# -*- coding:UTF-8 -*-

def tallenna_tulos(tiedoston_nimi, kotijoukkue, vierasjoukkue, pisteet_koti, pisteet_vieras):
    """Tallentaa tuloksen muodossa ensimmäisen joukkueen nimi:ensimmäisen joukkueen pisteet;toisen joukkueen nimi: toisen joukkueen pisteet"""
    tiedosto = open(tiedoston_nimi, "a")
    try:
        tiedosto.write("%s:%i;%s:%i\n" % (kotijoukkue, pisteet_koti, vierasjoukkue, pisteet_vieras))
    finally:
        tiedosto.close()
        
def nayta_tulokset(tiedoston_nimi):
    """Muuttaa merkkijonon muotoon: ensimmäisen joukkueen nimi ja pisteet - toisen joukkueen nimi ja pisteet"""
    tiedosto = open(tiedoston_nimi)
    rivit = tiedosto.readlines()
    for rivi in rivit:
        joukkueet = rivi.rstrip().split(";", 1)
        kotijoukkue_ja_pisteet = joukkueet[0]
        vierasjoukkue_ja_pisteet = joukkueet[1]
        kotijoukkue = kotijoukkue_ja_pisteet.split(":")
        vierasjoukkue = vierasjoukkue_ja_pisteet.split(":")
        joukkue_koti = kotijoukkue[0]
        pisteet_koti = int(kotijoukkue[1])
        joukkue_vieras = vierasjoukkue[0]
        pisteet_vieras = int(vierasjoukkue[1])
        tulos = ("%s" + " " + "%i" + " - " + "%i" + " " + "%s") % (joukkue_koti, pisteet_koti, pisteet_vieras, joukkue_vieras)
        print tulos
    tiedosto.close()
    
def laske_pisteet(tiedoston_nimi):
    sanakirja = {}
    avain = []
    arvo = []
    tiedosto = open(tiedoston_nimi)
    rivit = tiedosto.readlines()
    for rivi in rivit:
        rivi = rivi.rstrip().split(";", 1)
        for parit in rivi:
            avain, arvo = parit.rstrip().split(":", 1)
            arvo = int(arvo)
            try:
                sanakirja[avain] += arvo
            except KeyError:
                sanakirja[avain] = arvo
    return sanakirja