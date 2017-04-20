# -*- coding:UTF-8 -*-

sarja_vastus = []
rinnan_vastus = []

def laske_sarja((sarja_vastus)):
    summa_sarja = int(sum(sarja_vastus))
    return summa_sarja

def laske_rinnan(rinnan_vastus):
    rinnan_vastus_kaanteisarvo = []
    for summa in rinnan_vastus[:]:
        rinnan_vastus_kaanteisarvo.append(summa ** (-1))
    summa_rinnan = (sum(rinnan_vastus_kaanteisarvo)) ** (-1)
    return summa_rinnan

while True:
    vastus_arvo = raw_input("Anna vastusarvo: ")
    if not vastus_arvo:
        break
    elif vastus_arvo.isdigit() and float(vastus_arvo) > 0:
        sarja_vastus.append(float(vastus_arvo))
        rinnan_vastus.append(float(vastus_arvo))
    else:
        print "Ei kelpaa. Kokeile uudestaan." 

if len(rinnan_vastus) > 0:
      sarjaan = int(laske_sarja(sarja_vastus))
      rinnan = float(laske_rinnan(rinnan_vastus))
      print 
      print "Sarjaresistanssi: ", sarjaan
      print "Rinnakkaisresistanssi: ", rinnan