otsikko = raw_input("Kirjoita otsikko: ").title()
viivamerkit = raw_input("Valitse alleviivausmerkki tai -merkit: ")
viivan_pituus = len(otsikko) / len(viivamerkit)
alleviivaus = viivan_pituus * viivamerkit
print otsikko
print alleviivaus