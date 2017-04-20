# -*- coding: UTF-8 -*-

syote = raw_input("Anna luku: ")
if not syote.isdigit():
    print "%s ei ole luku" % syote
elif syote.isdigit():
    luku = int(syote)
    tulos = luku ** 2
    print "%s potenssiin 2 on %s" % (syote, tulos)