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
```py
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
```py
def parcours_prefixe(racine):
    p = creer_pile()
    empile(p, racine)
    cur_node = None

    while !pile_vide(p):
        cur_node = sommet(p)
        depile(p)
        print(cur_node.val)
        if cur_node.fd:
            empile(cur_node.fd)
        if cur_node.fg:
            empile(cur_node.fg)
```

### Parcours infixe
On parcourt récursivement selon cette règle :

- On passe au fils gauche et on applique cette règle.
- On affiche le noeud courant.
- On passe au fils droit et on applique cette règle.

_Ce parcours permet de retourner une liste ordonnée en parcourant un ABR (Arbre Binaire de Recherche)._

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

#### Implémentation itérative
```py
def parcours_infixe(racine):
    p = creer_pile()
    empile(p, racine)
    cur_node = None
    while !pile_vide(p):
        cur_node = sommet(p)
        depile(p)
        if cur_node.fd:
            empile(p, cur_node.fd)
        if not cur_node.fg:
            print(cur_node.val)
        else:
            empile(p, cur_node)
            empile(p, cur_node.fg)
# Ne fonctionne pas pour le moment... En recherche d'idée !
```

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

### Insérer une valeur dans un ABR
```py
def planter(racine, val):
    if val <= racine.val:
        if racine.fg:
            planter(racine.fg, val)
        else:
            racine.fg = new Noeud(val=val, fg=None, fd=None)
    else:
        if racine.fd:
            planter(racine.fd, val)
        else:
            racine.fd = new Noeud(val=val, fg=None, fd=None)
```

### Rechercher dans un ABR
```py
def recherche(racine, val):
    cur_node = racine
    while cur_node:
        if cur_node.val == val:
            return True
        else if cur_node.val > val:
            cur_node = cur_node.fg
        else:
            cur_node = cur_node.fd
    return False
```

### Supprimer un élément d'un ABR
```py
def suppression(racine, val):
    # Il faut remplacer la valeur supprimée par la plus petite valeur
    # de son sous-arbre droit ou la plus grande de son sous-arbre gauche.
    # Si cette valeur de remplacement est une feuille, c'est cool.
    # Sinon, il faut faire ça en cascade.
    cur_node = racine
    if cur_node.val == val:

    while cur_node:
        if cur_node.val > val:
            if cur_node.fg.val == val:
                if is_feuille(cur_node.fg):
                    cur_node.fg = None
                    return
                else if (is_feuille(biggest_node(cur_node.fg.fg))):
                    biggest = biggest_node(cur_node.fg.fg)
                    replace(cur_node.fg, biggest)
                    return
                else:
                    smallest = smallest_node(cur_node.fg.fd)
                    replace(cur_node.fg, smallest)
                    return
            else:
                cur_node = cur_node.fg
        else:
            if cur_node.fd.val == val:
                if is_feuille(cur_node.fd):
                    cur_node.fd = None
                    return
                else if (is_feuille(biggest_node(cur_node.fd.fg))):
                    biggest = biggest_node(cur_node.fg.fg)
                    replace(cur_node.fd, biggest)
                    return
                else:
                    smallest = smallest_node(cur_node.fd.fd)
                    replace(cur_node.fd, smallest)
                    return
            else:
                cur_node = cur_node.fd
```

```py
def biggest_node(racine):
    cur_node = cur_node
    if cur_node:
        while cur_node.fd:
            cur_node = cur_node.fd
    return cur_node
```

```py
def smallest_node(racine):
    if cur_node:
        while cur_node.fg:
            cur_node = cur_node.fg
    return cur_node
```

```py
def is_feuille(el):
    return !el.fg and !el.fd
```

```py
def replace(node, replacer):
    node.val = replacer.val
    supprimer(replacer.val)
```