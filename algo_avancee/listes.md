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

```python
def insereTrie(tete, maillon):
    """
    : entrées
    :   tete : Maillon
    :   maillon : Maillon
    """
    # Début
    if tete is None:
        tete = maillon
    else:
        trouve = False
        if maillon.val <= tete.val:
            maillon.suivant = tete
            tete = maillon
            trouve = True
        # endif

        if not trouve:
            ptr = tete
            while ptr.suivant is not None and not trouve:
                if maillon.val <= ptr.suivant.val and maillon.val >= ptr.val:
                    trouve = True
                    maillon.suivant = ptr.suivant
                    ptr.suivant = maillon
                ptr = ptr.suivant
            # endwhile
            if not trouve:
                ptr.suivant = maillon
        # endif
    # endif
    # Fin
```

```python
def supprimer(tete, valeur):
    """
    : entrées
    :   tete : Maillon
    :   valeur : X
    """
    # Début
    if tete is not None:
        ptr = tete
        precedent = None
        trouve = False
        if tete.val == valeur:
            trouve = True
        while ptr.suivant is not None and not trouve:
            precedent = ptr
            if ptr.suivant.val == valeur:
                trouve = True
            ptr = ptr.suivant
        # endwhile
        if (not trouve and ptr.val == valeur) or trouve:
            precedent.suivant = ptr.suivant
            free(ptr)
    # endif
    # Fin
```

```python
def combiner(tete1, tete2):
    """
    : entrées
    :   tete1, tete2 : Maillon
    : precondition :
    : Les deux listes sont triées
    """
    # Début
    if not tete1:
        return tete2
    elif not tete2:
        return tete1
    # endif

    tete3 = new Maillon()
    tete3.val = tete1.val if tete1.val <= tete2.val else tete2.val
    tete3.suivant = None
    ptr1, ptr2, ptr3 = tete1, tete2, tete3
    while ptr1 or ptr2:
        ptr3.suivant = new Maillon()
        if not ptr2 and ptr1:
            ptr3.suivant.val = ptr1.val
            ptr1 = ptr1.suivant
        elif not ptr1:
            ptr3.suivant.val = ptr2.val
            ptr2 = ptr2.suivant
        else:
            if (ptr1.val <= ptr2.val):
                ptr3.suivant.val = ptr1.val
                ptr1 = ptr1.suivant
            else:
                ptr3.suivant.val = ptr2.val
                ptr2 = ptr2.suivant
            # endif
        # endif
    # endwhile
    return tete3
    # Fin
```

```python
def autreCombiner(tete1, tete2):
    """
    : entrées
    :   tete1, tete2 : Maillon
    : precondition :
    : Les deux listes sont triées
    """
    # Début
    if not tete1:
        return tete2
    elif not tete2:
        return tete1
    # endif

    tete3 = new Maillon()
    tete3.val = tete1.val
    tete3.suivant = None
    ptr1, ptr2, ptr3 = tete1, tete2, tete3

    # On copie la liste 1 dans celle qu'on retourne.
    while ptr1:
        ptr3.suivant = new Maillon()
        ptr3.suivant.val = ptr1.val
        ptr1 = ptr1.suivant
        ptr3 = ptr3.suivant
    # endwhile

    # On utilise l'algo précédemment écrit pour insérer la deuxième.
    while ptr2:
        insereTrie(tete3, ptr2)
        ptr2 = ptr2.suivant
    # endwhile

    return tete3
```


