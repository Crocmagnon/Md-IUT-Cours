# Les étapes de la gestion de projet informatique
## Étapes
1. Estimation de la charge
2. Signature du contrat
    - Étude détaillée de la charge => Méhode analytique
    - Délai minimal techniquement nécessaire => Méthode PERT
        - Délai opérationnel
        - Nb de collaborateurs à prévoir = $\frac{\textrm{Charge estimée}}{\textrm{Délai opérationnel}}$
3. En fonction du calendrier des personnels, on décide qui fait quoi (affectation)
4. On construit un planning, ou calendrier de réalisation, ou diagramme de GANTT
5. Pilotage du projet
    - Suivi de l'avancement
    - Gestion des aléas

## Signature du contrat
Le contrat va être signé, on procède à l'analyse détaillée de la durée.
### Niveaux de démarrage
Tâches ancêtres | Tâches | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
----------------|--------|---|---|---|---|---|---|---|
-               | A      | A |   |   |   |   |   |   |
A               | B      |   | B |   |   |   |   |   |
B               | C      |   |   | C |   |   |   |   |
C               | D      |   |   |   | D |   |   |   |
D, F            | E      |   |   |   |   | E |   |   |
C               | F      |   |   |   | F |   |   |   |
B               | G      |   |   | G |   |   |   |   |
G               | H      |   |   |   | H |   |   |   |
H, F            | I      |   |   |   |   | I |   |   |
I, E            | J      |   |   |   |   |   | J |   |
J, M            | K      |   |   |   |   |   |   | K |
-               | L      | L |   |   |   |   |   |   |
L, H            | M      |   |   |   |   | M |   |   |

### Méthode PERT
On calcule le délai minimum techniquement nécessaire à condition de disposer de toutes les ressources nécessaires.

_(cf. scan)_

On peut calculer la marge dont dispose chaque tâche.  
La séquence des tâches sans marge s'appelle le __chemin critique__.

Remarques :

* On ne doit pas s'entendre avec le client sur le délai _fin au plus tôt_
    1. Pour pallier les inévitables aléas.
    2. Pour lisser la charge des ressources utilisées => Allongement du délai nécessaire.

## Diagramme de GANTT
_(Tu sais faire, je vais pas te le dessiner)_

## Pilotage de projet
