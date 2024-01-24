from random import randint
import random

populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 13, "name" : "Brice" },
    { "id" : 14, "name" : "Alice" },
    { "id" : 15, "name" : "Sophia" },
    { "id" : 16, "name" : "Rasmus" },
    { "id" : 18, "name" : "Taylor" },
    { "id" : 19, "name" : "Olivia" },
    { "id" : 20, "name" : "Jessica" },
    { "id" : 21, "name" : "Anna" },
    { "id" : 22, "name" : "Samantha" },
    { "id" : 23, "name" : "Grace" },
    { "id" : 24, "name" : "Anna" },
    { "id" : 25, "name" : "Alexis" },
    { "id" : 26, "name" : "Madison" },
    { "id" : 27, "name" : "Nicole" },
    { "id" : 28, "name" : "Amanda" },
    { "id" : 29, "name" : "Haley" }  
]

# 1.Ajoutez un champ lenChar qui détermine la longueur de chaque nom.

for person in populations:
    person['lenChar'] = len(person['name'])

# 2.Ajoutez un champ rate, puis respectivement attribuer pour chaque personne, des valeurs aléatoires comprises entre 1 et 100.
for person in populations:
    person['rate'] = randint(1, 100)

# 3.Déterminez les 4 personnes qui ont les meilleurs valeurs de rate.
sortedPopulation =  sorted(populations, key=lambda x:x['rate'], reverse=True)

top4 = sortedPopulation[:4]

# 4.Attribuez une augmentation de 0.1% à chacune des valeurs ( rate ).
for person in populations:
    newRate = person['rate']*1.001
    person['rate'] = round(newRate, 2)

#Autre méthode plus optimisée
populations = list( map(
    lambda person : {**person, 'rate' : person['rate']*1.001},
    populations
))

# 5.Créez une fonction qui permet de tirer de manière aléatoire une personne.
def randomPerson():
    return random.choice(populations)

# 6.Ordonnez par ordre croissant dans une liste s de tuples, les personnes en fonction de leur rate respectif.
s=[]
triCroissant = sorted(populations, key=lambda x:x['rate'])
for person in triCroissant:
    s.append((person['name'], person['rate']))

# 7.Trouvez la valeur centrale, la valeur centrale partage en deux la série de valeurs rates ordonnées.
halfLength = int(len(s)/2)
if halfLength % 2:
    median = round(s[halfLength][1],2)
else :
    value1 = s[halfLength][1]
    value2 = s[halfLength+1][1]
    median = round((value1 + value2)/2, 2)

print(f"médiane : {median}")

# 8.Partionnez la liste s en quatre parties distinctes. Que représente à votre avis la valeur centrale déterminée dans la question précédente.
part1Index = len(s) // 4
part2Index = 2 * part1Index
part3Index = 3 * part1Index

part1 = s[:part1Index]
part2 = s[part1Index:part2Index]
part3 = s[part2Index:part3Index]
part4 = s[part3Index:]

print(f'partie 1 : {part1}')
print(f'partie 2 : {part2}')
print(f'partie 3 : {part3}')
print(f'partie 4 : {part4}')

# 9.Concluez sur la répartition de ces valeurs. Que pensez vous de la valeur centrale par rapport à la moyenne ( à calculer ) de la série de valeurs rates.
somme = 0
for rate in s:
    somme += rate[1]

moyenne = round(somme // len(s),2)
print(f"Moyenne : {moyenne} / Median : {median}")

# La médiane divise en deux parts égales une série de valeurs.
# Tandis que la moyenne est la somme de toutes les valeurs, divisée par le nombre de valeurs.