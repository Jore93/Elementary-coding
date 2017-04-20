# -*- coding: UTF-8 -*-
 
x1 = float(raw_input("Anna ensimmäisen pisteen x-koordinaatti: "))
y1 = float(raw_input("Anna ensimmäisen pisteen y-koordinaatti: "))
x2 = float(raw_input("Anna toisen pisteen x-koordinaatti: "))
y2 = float(raw_input("Anna toisen pisteen y-koordinaatti: "))
if x1 == x2 and y1 == y2:
    print "Nämähän ovat yksi ja sama piste!"
elif x2 - x1 == 0:
    print "Pisteiden (%.3f, %.3f) ja (%.3f, %.3f) kautta kulkeva suora on pystysuora, ei kulmakerrointa." % (x1, y1, x2, y2)
else:
    k = float((y2 - y1) / (x2 - x1))
    if k < 0:
        print "Pisteiden (%.3f, %.3f) ja (%.3f, %.3f) kautta kulkeva suora on laskeva, kulmakerroin = %.3f." % (x1, y1, x2, y2, k)
    elif k > 0:
        print "Pisteiden (%.3f, %.3f) ja (%.3f, %.3f) kautta kulkeva suora on nouseva, kulmakerroin = %.3f." % (x1, y1, x2, y2, k)
    elif not k != 0:
        print "Pisteiden (%.3f, %.3f) ja (%.3f, %.3f) kautta kulkeva suora on vaakasuora, kulmakerroin = %.3f." % (x1, y1, x2, y2, k)