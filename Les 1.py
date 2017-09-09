#Exercise 1_2
#a
print(len('Supercalifragilisticexpialidocious'))
#b
print('ice' in 'Supercalifragilisticexpialidocious')
#c
print(len('Antidisestablishmentarianism') > len('Honorificabilitudinitatibus'))
#d
lst = ['Berlioz', 'Borodin', 'Brian','Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
lst.sort()
print(lst)

#Exercise 1_3
#1
a = 6
b = 7
print(a)
print(b)
#2
c = (a + b)/2
print(c)
#3
inventaris = [ 'papier', 'nietjes', 'pennen']
print(inventaris)
#4
voornaam = 'Jelle'
tussenvoegsel = ''
achternaam = ' Meijer'
#5
mijnnaam = voornaam +tussenvoegsel + achternaam
print(mijnnaam)

#Exercise 1_4
#1
print(6.75 > a and 6.75 < b)
#2
print(len(inventaris) > (len(mijnnaam)*5))
#3
print(len(inventaris) == 0)
print(len(inventaris) > 10)

#Exercise 1_5
#1
favorieten = ['Linkin Park']
print(favorieten)
#2
favorieten.append('Of Mice & Men')
print(favorieten)
#3
favorieten[1] = 'Crown The Empire'
print(favorieten)

#Exercise 1_6
list = [3,7,-2,12]
print(list)
print(max(list)-min(list))

list = [3,7,-2,10]
print(list)
print(max(list)-min(list))