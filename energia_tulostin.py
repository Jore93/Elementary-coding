# -*- coding: utf-8 -*-

def tulosta_energia(merkkijono, liike_energia=0):
    """Tulostaa annetun liikkuvan kohteen ja sen liike-energian merkkijonoon muotoiltuna."""
    print "%s saa liike-energian %.3f J." % (merkkijono.title(), liike_energia)
tulosta_energia(merkkijono="kissa", liike_energia=1000)
tulosta_energia(merkkijono="ihminen", liike_energia=3500)
tulosta_energia(merkkijono="AUTO", liike_energia=300000.0009)