'''
Napisati regex za provjeru validnosti unosa e-maila.E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
'''


import re

regex_email = '^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
regex_eduid = '^[a-z]{1}[a-zA-Z]+\d*@sum\.ba$'

unos_email=input("| Unesite Email: ")


if re.match(regex_email, unos_email):
    print("Email adresa je ispravna.")
else:
    print("Email adresa nije ispravna.")

print("\n")   
unos_eduid=input("| Unesite EduId: ")

if re.match(regex_eduid, unos_eduid):
    print("EduId je ispravan.")
else:
    print("EduId nije ispravan.")

