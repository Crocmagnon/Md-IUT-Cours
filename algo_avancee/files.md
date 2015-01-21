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
```
Maillon struct (
    valeur : INT
    suivant : SAME)

File struct (
    debut : Maillon
    Fin : Maillon)
```

### Définition (listes)
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

#### 1ère solution
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