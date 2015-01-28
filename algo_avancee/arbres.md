# Les arbres
À la différences des listes ou des files, qui sont des relations linéaires entre les données, ici on peut avoir des relations non linéaires.

## Définition
Un graphe G = (X, E) est défini par :

- L'ensemble X des sommets (noeuds)
- L'ensemble E des arêtes

Un arbre A est un graphe tel que A est connexe (il existe toujours un chemin entre deux feuilles de l'arbre).

On ne trouve pas de cycle dans les arbres (les branches ne se recroisent pas en un noeud).

Un noeud dans un arbre a des fils (les noeuds en dessous de lui) et des parents (les noeuds au dessus).

Un arbre est un graphe à niveaux (chaque fils est au niveau n+1, en considérant que son parent est au niveau n). La hauteur d'un arbre est le max des niveaux des feuilles.

Si on dispose de la racine, on a accès à tout l'arbre.

Un arbre binaire est un arbre dans lequel chaque noeud a au plus deux fils.

```
Noeud struct(
    fd: SAME
    val: INT
    fg: SAME)
```

## Parcours d'arbres binaires
On a quatre types de parcours.

### Parcours par niveau
Chaque niveau va être parcouru linéairement (toutes les valeurs du même niveau de gauche à droite à la suite).

#### Implémentation itérative
```python
def parcours_niveau(racine):
    f = creer_file()
    e_cour = racine
    ajout_fin_file(f, e_cour)
    while !file_vide(f):
        e_cour = debut_file(f)
        retirer_debut_file(f)
        print(e_cour.val)
        if e_cour.fg:
            ajout_fin_file(f, e_cour.fg)
        if e_cour.fd:
            ajout_fin_file(f, e_cour.fd)
```

### Parcours préfixe
On parcourt récursivement selon cette règle :

- On affiche le noeud courant.
- On passe au fils gauche et on applique cette règle.
- On passe au fils droit et on applique cette règle.

Ainsi, pour un arbre comme celui-ci :

```
      A
    /   \
   /     \
  B       C
 / \     /
D   E   F
```

On aura : `A B D E C F`

#### Implémentation itérative
- On commence par la racine, on l'ajoute à la pile et on l'affiche.
- On traite ensuite son fils gauche, s'il a un fils droit on l'ajoute à la pile.
- On l'affiche, et on continue ainsi jusqu'à ne plus avoir de fils gauche.
- On prend alors le premier élément de la pile et on traite son fils droit.
- Et ainsi de suite.

```python
def parcours_prefixe(racine):
    pass
```

### Parcours infixe
On parcourt récursivement selon cette règle :

- On passe au fils gauche et on applique cette règle.
- On affiche le noeud courant.
- On passe au fils droit et on applique cette règle.

Ainsi, pour un arbre comme celui-ci :

```
      A
    /   \
   /     \
  B       C
 / \     /
D   E   F
```

On aura : `D B E A F C`

### Parcours postfixe
On parcourt récursivement selon cette règle :

- On passe au fils gauche et on applique cette règle.
- On passe au fils droit et on applique cette règle.
- On affiche le noeud courant.

Ainsi, pour un arbre comme celui-ci :

```
      A
    /   \
   /     \
  B       C
 / \     /
D   E   F
```

On aura : `D E B F C A`