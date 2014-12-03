# Algo avancée - Listes
## Problématique
Les tableaux ont une taille fixe. Ce n'est pas intéressant pour des volumes variables de données. En effet, l'espace mémoire est une ressource. Et il ne faut pas gaspiller les ressources.  
L'idée est de trouver une manière dynamique de demander de l'espace mémoire en fonction des données à stocker. Le problème est qu'on a plus de lien entre les cases. Il faut alors également réserver de l'espace dans la "case" pour le chaînage (quel est l'élément suivant).  
Cette structure de données correspond aux listes.

L'avantage des listes est son dynamisme. Son inconvénient est la lenteur de l'accès aux données (on est obligés de passer par la tête de la liste puis par toutes les cases suivantes pour accéder à une valeur).

## Exercices
Écrire un algo de création de LLC (Liste Linéaire Chaînée) avec des valeurs saisies par l'utilisateur.

```python
def creationliste(nbval):
    """
    : declaration
    :   ptr : Maillon
    :   cpt, val : int
    : entrée nbval : int
    : sortie tete : Maillon
    : Précondition
    :   nbval > 0
    """
    #Début
    cpt = 0
    for cpt in range(nbval):
        print("valeur n°", cpt)
        val = int(input())

        if cpt == 0:
            tete = new Maillon()
            tete.val = val
            ptr = tete
        else:
            ptr.suivant = new Maillon()
            ptr = ptr.suivant
            ptr.val = val
        #endif
    #endfor

    ptr.suivant = None
    return(tete)
    #Fin
```

Écrire deux algos de recherche dans une liste : booléen en sortie et maillon en sortie

```python
def recherche_booleen(tete, valeur):
    """
    : declaration
    :   ptr : Maillon
    : entrées
    :   tete : Maillon
    :   valeur : X
    """
    # Début
    ptr = tete
    while ptr is not None:
        if ptr.val == valeur:
            return True
        ptr = ptr.suivant
    # endwhile
    return False
    # Fin
```

```python
def recherche_maillon(tete, valeur):
    """
    : entrées
    :   tete : Maillon
    :   valeur : X
    : sortie
    :   ptr : Maillon
    """
    # Début
    ptr = tete
    while ptr is not None:
        if ptr.val == valeur:
            return ptr
        ptr = ptr.suivant
    # endwhile
    return None
    # Fin
```

Écrire un algo qui compte le nombre d'éléments dans une liste

```python
def compte(tete):
    """
    : entrées
    :   tete : Maillon
    : sortie
    :   compte : int
    """
    # Début
    ptr = tete
    compte = 0
    while ptr is not None:
        compte += 1
        ptr = ptr.suivant
    # endwhile
    return compte
    # Fin
```
