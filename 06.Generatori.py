'''
Napraviti generator funkcije za ispis
svih parnih i svih neparnih brojeva manjih
od prosljeđenog parametra.
'''


def parni_brojevi(broj):
    for i in range (broj):
        if i%2==0:
            parni=i
            yield parni,None
            
        else:
            neparni=i
            yield None,neparni
            
            
broj=10
pn=list(parni_brojevi(broj))
print("Parni brojevi su: ")
for a,b in pn:
    if a:
        print("-",a)
print("------------------------")
print("Neparni brojevi su: ")

for a,b in pn:
    if b:
        print("-",b)
