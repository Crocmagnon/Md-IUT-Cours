# Les files
Le principe est celui des files d'attentes : premier arrivé, premier sorti.

## Primitives
### Déclaration
```python
f = creer_pile()
bool : file_vide(f)
bool : file_pleine(f)
ajout_fin_file()
elt = debut_file()
retirer_debut_file()
```

### Définition (listes)
```
Maillon struct (
    valeur : INT
    suivant : SAME)

File struct (
    debut : Maillon
    fin : Maillon)
```
```python
def creer_file():
    file = File(debut=None, fin=None)
    return file

def file_vide(file):
    return file.debut is None

def file_pleine(file):
    return False

def ajout_fin_file(file, elt):
    mail = Maillon(valeur=elt, suivant=None)
    if file.fin:
        file.fin.suivant = mail
    else:
        file.debut = mail
    file.fin = mail

def debut_file(file):
    return file.debut.valeur

def retirer_debut_file(file):
    mail = file.debut
    file.debut = file.debut.suivant
    if not file.debut:
        file.fin = None
    free(mail)
```

### Définition (tableaux)
```
File struct (
    deb : int
    fin : int
    tab : tableau de X)
```
```python
# On considèrera que la constante MAX est définie et correspond à la taille maximale possible d'un tableau

def creer_file():
    file = File(deb=-1, fin=-1, tab=numpy.empty(MAX))
    # Checker syntaxe, il manque un paramètre
    return file

def file_vide(file):
    return file.deb == -1

def file_pleine(file):
    return (file.fin + 1) % MAX == file.deb

def ajout_fin_file(file, elt):
    if file.deb == -1:
        file.deb += 1
        file.tab[file.deb] = elt
    else:
        file.tab[file.fin + 1] = elt
    file.fin += 1

def debut_file(file):
    return file.tab[file.deb]

def retirer_debut_file(file):
    if file.deb == file.fin:
        file.deb = -1
        file.fin = -1
    else:
        file.deb += 1
        file.deb %= MAX
```

`TODO : Implémenter ça pour le 1/02`

## Exercices
### Exercice 1
Écrire un algo qui affiche les éléments d'une file en la conservant.

#### 1ère solution
Ici on passe par une autre file : On défile chaque élément pour le mettre dans l'autre file, on affiche chaque élément défilé, puis on change la référence de la file.
```python
def affiche_file(f):
    f_temp = creer_file()

    while !file_vide(f):
        print(debut_file(f))
        ajouter_fin_file(f_temp, debut_file(f))
        retirer_debut_file(f)

    f = f_temp
    return f
```

#### 2ème solution
Cette solution est dite "en place", parce qu'on n'a pas besoin d'une file supplémentaire. On défile chaque élément pour le rajouter à la fin de la file.
On définit préalablement un maillon qui indiquera la fin de la file pour ne pas répéter indéfiniment.
```python
def afficher_file(f):
    """
    On définit une str "***" qui marque la fin de la file.
    La file ne doit pas contenir cet élément.
    """
    fin_file = "***"
    ajouter_fin_file(f, fin_file)

    while (debut_file != fin_file):
        print(debut_file(f))
        ajouter_fin_file(f, debut_file(f))
        retirer_debut_file(f)

    retirer_debut_file(f) # On retire le marqueur de fin.
```

### Exercice 2
Écrire une fonction récursive de recherche dans une file non triée.

#### Solution
Ici la file est modifiée, tous les éléments précédant l'élément recherché sont supprimés.
```python
def rech_recursive(f, elt):
    if file_vide(f):
        return False
    if debut_file(f) == elt:
        return True
    
    retirer_debut_file(f)
    return(rech_recursive(f, elt))
```

### Exercice 3
Écrire une fonction qui inverse une file.

#### Solution
```python
def inverse(f):
    p = creer_pile()
    while !file_vide(f):
        empile(p, debut_file(f))
        retirer_debut_file(f)

    while !pile_vide(p):
        ajouter_fin_file(f, sommet(p))
        depile(p)

    return(f)
```

### Exercice 4
Soit une file d'entiers. Écrire un algorithme qui réordonne la file de sorte que les entiers pairs soient en début de file.

#### Solution
```python
def tri_pairs(f):
    f_pairs = creer_file()
    f_impairs = creer_file()
    
    while !file_vide(f):
        debut = debut_file(f)
        if debut % 2 == 0:
            ajouter_fin_file(f_pairs, debut)
        else:
            ajouter_fin_file(f,_impairs debut)
        
        retirer_debut_file(f)

    while !file_vide(f_impairs):
        ajouter_fin_file(f_pairs, debut_file(f_impairs))
        retirer_fin_file(f_impairs)
```