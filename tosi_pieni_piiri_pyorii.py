# -*- coding:UTF-8 -*-

vastukset = []

def laske_sarja(vastukset):
    kokonaisresistanssi = sum(vastukset)
    return kokonaisresistanssi
    
def laske_jannitteet(vastukset, virta):
    vastus_jannite = []
    for vastus in vastukset:
        jannite_yli = virta * vastus
        vastus_jannite.append(jannite_yli)
    return vastus_jannite  

def laske_virta(jannite, kokonaisresistanssi):
    virta = jannite / kokonaisresistanssi 
    return virta    

if __name__ == "__main__":
    while True:
        vastus = raw_input("Syötä vastusarvo (kokonaisluku) : ")
        if vastus.isdigit() and float(vastus) > 0:
            vastukset.append(float(vastus))
        elif vastus.upper() == "Q":
            break
        else:
            print "Epäkelpo arvo, yritä uudelleen."

    kokoaisresistanssi = laske_sarja(vastukset)
    jannite = int(raw_input("Anna jännite: "))
    virta = laske_virta(jannite, kokoaisresistanssi)
    vastus_jannite = laske_jannitteet(vastukset, virta)
    print
    print "Sarjaankytkennän virta on %.3fA" % virta
    print "Vastusten yli olevat jännitteet (ensiksi syötetty vastus ensin) : \n%s" % vastus_jannite