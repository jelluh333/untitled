#Exercise 2_1
letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
letters = list(letters)
letters.sort()
a =(letters.count('A'))
b =(letters.count('B'))
c =(letters.count('C'))
totaal = [a,b,c]
print(totaal)

#Exercise 2_2
cijferICOR = 6
cijferPROG = 7
cijferCSN = 8

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3

beloning = (cijferICOR + cijferPROG + cijferCSN) *30

overzicht = ('Mijn cijfers (gemiddeld een ' + str(gemiddelde)+ ') leveren een beloning van €' +str(beloning)+ ' op!')
print(overzicht)

#Exercise 2_3

print(0 == (1 == 2))
print(2 + (3 == 4) + 5 == 7)
print(1 < (-1 == 3 > 4))

#Exercise 2_4

uurloon = input('Wat verdien je per uur?')
aantal_uur = input('Hoeveel uur heb je gewerkt?')
totaal_loon = int(uurloon) * int(aantal_uur)
print(str(uurloon) + ' uur werken levert '+ str(totaal_loon) +' Euro op')