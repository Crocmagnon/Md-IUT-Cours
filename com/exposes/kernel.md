# Le kernel dans un OS
Différents OS : OS X, Windows, Linux

## Composantes communes
- Processeur
- Mémoire
- IO
- Appels système
- Erreurs

### Processeur
Gère l'ordonnancement entre les tâches : qui fait quoi et quand ?

### Mémoire
RAM (Random Access Memory) : Permet de stocker des données temporairement. Un programme demande au système de la mémoire, le kernel lui donne une part.

### Entrées / Sorties
Tout ce qui est connecté à l'ordinateur. Le kernel doit pouvoir gérer les divers composants.

### Appels système (~ interruptions)
L'utilisateur lance un processus. Il demande à l'OS de lire un fichier mais ne peut pas le faire directement. Il fait un appel système et ce dernier gère l'autorisation ou non de la commande.

### Erreurs
Dans la continuité des Appels système. Si on essaye d'accéder à une zone mémoire interdite, le kernel refuse la demande et coupe le programme.

## Le démarrage
1. On appuie sur le bouton, le BIOS est le premier programme à être chargé. Il est stocké dans une puce sur la carte mère.
2. Le BIOS appelle le bootloader (stocké sur le DD), qui lui-même appelle l'image noyau compressée (<1Mo).
3. L'image système se décompresse elle-même (le début de son code contient sa routine de décompression).
4. La première chose à être mise en place est la pagination pour gérer la RAM.
5. On détecte ensuite le CPU pour charger l'ordonanceur.
6. Chargement des drivers en mémoire puis initialisation matérielles nécessaires
7. On charge l'OS et on passe la main au premier processus utilisateur qui déclenche en cascade tous les autres.

## Différents noyaux
### Monolithique
#### Monolithique pur
Très rapide.  
Aujourd'hui obsolète. Très lourd (> 6 millions de lignes de code).

#### Monolithique modulaire
Toujours très rapide.
Sépare les parties moins critiques.  
Toujours très lourd.

### Micro-noyaux
Plus stable qu'un monolithique, car dans l'espace noyau ne se trouve que ce qui est critique pour l'OS. Le reste est dans l'espace utilisateur.  
Plus lent car utilise des messages plus lourds entre processus.  
Plus léger et plus facile à entretenir.
#### Micro-noyaux enrichis (Ubuntu, Windows)
Le reste n'est plus dans l'espace utilisateur mais dans le micro noyau enrichi.

### Noyaux hybrides (OS X)
Le meilleur des deux mondes : rapide et stable.  
On a rapatrié certains services dans le noyau hybride, les autres sont dans l'espace utilisateur.

## Différents types de noyaux : temps réel (OS X) ou non
Ils sont fonctionnellement spécialisés. Très utilisé dans l'électronique embarquée (ABS dans les voitures, navettes spatiales, ...). Ils garantissent qu'un processus critique puisse bénéficier de tout le temps processeur si besoin.

## Historique
### Années 60
IBM fait des machines pour les entreprises mais on est à chaque fois obligés de rédemarrer l'ordinateur pour charger un nouveau programme.  
IBM crée alors le premier environnement d'exploitation et y intègre la gestion des I/O.
### Années 70
UNIX voit le jour grâce à l'invention du C : portabilité et abstraction du matériel.
### Années 80
Les premiers problèmes de sécurité apparaissent. Les ordinateurs travaillent encore en mode réel à cette époque (pas de pagination, on adresse directement les données dans la RAM).  
On invente alors le concept de mémoire virtuelle (MMU : Memory Management Unit).
### Années 90
Les processeurs deviennent multitâches.
### Années 2000
Les processeurs deviennent multicoeurs : révision de l'ordonanceur, nouvelles contraintes.
### Années 2010
Virtualisation des systèmes plus répandue.