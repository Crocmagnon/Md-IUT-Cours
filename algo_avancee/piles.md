# Algo avancée - Listes

[TOC]

## Problématique
Les tableaux et les listes sont des structures basiques et ne permettent pas la résolution de certains problèmes.

## Les piles
Les piles sont comme une pile d'assiettes.  
On dispose de fonctions permettant les opérations sur les piles :

```python
p = creer_pile()
empiler(p, e)
depiler(p)
elt = sommet(p)
vide = pile_vide(p)
pleine = pile_pleine(p)
```

On peut modéliser les piles de différentes manières

### Modélisation liste
On peut voir les piles comme des listes :  
La tête s'appelle maintenant sommet, on empile en ajoutant un élément avant la tête, on dépile en enlevant le sommet et en le déplaçant.  
La pile ici ne sera jamais pleine.

```python
def creer_pile():
    p = Pile(sommet=None)
    return p


def pile_vide(p):
    return p.sommet == None


def empile(p, e):
    ptr = new_maillon()
    ptr.suivant = p.sommet
    ptr.valeur = e
    p.sommet = ptr
```

### Modélisation tableau
Renvoi au cours d'algo.

## Problèmes
### Bien parenthésé ?
On cherche à déterminer si une expression est bien parenthésée ou non. On va utiliser les piles pour résoudre ce problème :

```python
def check_parentheses(expression):
	pile = creer_pile()
	for car in expression:
    	if car == '(' or car == '[':
			empile(pile, car)
        elif car == ')':
      		if pile_vide(pile) or sommet(pile) != '(':
     			return False
    		depile(pile)
        elif car == ']':
      		if pile_vide(pile) or sommet(pile) != '[]':
     			return False
    		depile(pile)
		i += 1
    return pile_vide(pile)
```

### Fonction miroir 
```python
def miroir():
    pile = creer_pile()
    car = input("Saisir un caractère ")
    while car <= 'z' and car >= 'a' or car <= 'Z' and car >= 'A':
        empile(pile, car)
        car = input("Saisir un caractère ")

    while not pile_vide(pile):
    	print(sommet(pile), end="")
    	depile(pile)
    print()
```

### Fonction qui sert à rien
```python
def separate_car():
    chaine = input("Saisir une chaine : ")
    for car in chaine:
        print(car)
```