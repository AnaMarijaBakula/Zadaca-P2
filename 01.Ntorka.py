'''
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 
'''
import csv



with open('rezultati.csv', 'r') as file:
    redovi = file.readlines()
    studenti = []
    for linija in redovi:
        elementi = linija.strip().split(';')
        ime, prezime, bodovi, = elementi
        print (tuple(elementi))
        studenti.append((ime, prezime, int(bodovi)))

sortirano=sorted(studenti, key=lambda x: x[1])

ocjene={
    "Nedovoljan":[],
    "Dovoljan":[],
    "Dobar":[],
    "Vrlodobar":[],
    "Izvrstan":[]
    }


for ime,prezime, bodovi in sortirano:
    if bodovi < 50:
        ocjene["Nedovoljan"].append(prezime)
    elif bodovi < 66:
        ocjene["Dovoljan"].append(prezime)
    elif bodovi < 81:
        ocjene["Dobar"].append(prezime)
    elif bodovi < 91:
        ocjene["Vrlodobar"].append(prezime)
    else:
        ocjene["Izvrstan"].append(prezime)

print(ocjene)
