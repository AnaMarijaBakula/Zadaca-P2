'''
Koristeći listu imena iz prethodnog zadatka svakom studentu
generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
'''

import random

studenti=['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjene_st={}
prebrojano = {5:0,4:0,3:0,2:0,1:0}

for ime in studenti:
    ocjena=random.randint(1,5)
    ocjene_st[ime]=ocjena
    if ocjena in prebrojano:
        prebrojano[ocjena]+=1

print(prebrojano)
brojac=0
studenti_ocjene=0

print(prebrojano)
for ocjena in prebrojano:
    if ocjena>1:
        zbroj_ocjena=ocjena*prebrojano[ocjena]
        brojac+=zbroj_ocjena
        
        print(zbroj_ocjena)
        
print(brojac,len(studenti))       

print(brojac/len(studenti))
        
    
        
    

