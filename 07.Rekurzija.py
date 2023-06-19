'''
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.
'''

def zadnji(unos):
    if len(unos)==0:
        return ""
    if len(unos)==1:
        return unos
    else:
        return unos[-1]+zadnji(unos[:-1])

unos=input("Unesite rijec: ")
rez=zadnji(unos)
print(rez)
