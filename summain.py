# -*- coding:UTF-8 -*-

luvut = []

def summain(syote):
    """Laskee listan alkioiden summan."""
    summa = sum(syote)
    return summa
    
if __name__ == "__main__":
    import numbers
    while True:
        kysymys = raw_input("Anna luku: ")
        if numbers.real(kysymys):
            luvut.append(kysymys)
        if not kysymys:
            break    
    print summain(luvut)