imena =['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena =['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

import random


radnici = []


for i in range(15):
    radnik = {}
    radnik["ime"] = random.choice(imena)
    radnik["prezime"] = random.choice(prezimena)
    radnik["satnica"] = round(random.uniform(4, 6), 2)
    radnici.append(radnik)

print(radnici)

for radnik in radnici:
    radnik['tjedni_sati'] = random.randint(20, 30)

print(radnici)

isplate = []
for radnik in radnici:
    isplata = radnik["satnica"] * radnik["tjedni_sati"]
    mytuple = radnik["ime"], radnik["prezime"], round(isplata, 2)
    isplate.append(mytuple)
    
print(isplate)

iznos = 0
for ime, prezime, isplata in isplate:
    print(ime, prezime, isplata)
    iznos += isplata

broj_radnika =len(radnici)
prosjek=iznos/broj_radnika
print("\n|  Ukupno za isplatiti:", iznos,"\n")
print("|  Prosjecna isplata je: ",prosjek,"\n")
print("|  Isplata iznad prosjeka: \n")
for ime,prezime,isplata in isplate:
    if isplata>prosjek:
        print(ime,prezime)

