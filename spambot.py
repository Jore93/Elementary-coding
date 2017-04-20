# -*- coding: UTF-8 -*-
def luo_mainosposti(pohjat, tiedot):
    for i in tiedot:
         pohjat = pohjat.replace( "{{ %s }}" %i, tiedot[i])
    return pohjat
if __name__ == "__main__":
    tiedot = {"etunimi": "Justiina", "sukunimi": "Yli-Rima", "email": "justiina.yli-rima@student.example.com", "tuote": '"Pythonin kertausharjoitukset"', "tuotetyyppi": "kirja", "mainossana": "arvostettu", "hinta": "25,99 €"}
    pohjat = "To: \"{{ etunimi }} {{ sukunimi }}\" <{{ email }}>\n\nHei {{ etunimi }}!\n\nKiinnostavatko sinua {{ tuotetyyppi }}t? Nyt sinulla on\nainutlaatuinen mahdollisuus saada {{ mainossana }}\n{{ tuote }} järkyttävään\nalennushintaan {{ hinta }}!\n"
    print luo_mainosposti(pohjat, tiedot)