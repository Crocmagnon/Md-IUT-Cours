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
    if file.fin != None:
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