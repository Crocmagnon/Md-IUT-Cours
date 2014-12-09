# Diagramme de classe
On l'utilise pour montrer la structure statique du système et identifier les concepts propres au domaine (les concepts métier qui particient aux cas d'utilisation).

On l'utilise pendant tout le processus de modélisation. Les diagrammes de classe s'enrichissent : plus on avance dans la modélisation, plus ils sont détaillés.

Un diagramme de classe décrit les classes et les relations. Pour en construire un, il faut :

- Définir les classes et leurs responsabilités
    + Les classes -> Concepts métiers
    + Les attributs
    + Les méthodes
- Définir les relations entre ces classes

## Démarche
C'est un processus itératif : il faut itérer et affiner le modèle.

- Pas d'exactitude du modèle à la première réalisation
- Nécessité de réaliser des itérations continuelles
- Possibilité d'avoir différentes parties du modèle à différents stades d'achèvement
- Raffinements probables après l'achèvement d'autres modèles

On commence à un haut niveau d'abstraction, puis on enrchit le modèle

- Des données manipulées aux difféents éléments composant le système

## Démarche conseillée
- Identifier les classes et conserver celles qui sont pertinentes
    + Éviter d'être trop sélectif au départ
    + Éliminer les classes redondantes, sans intérêt
- Faire de même avec les associations
- Identifier les attributs
    + Ne pas pousser la recherche à l'extrême
    + Repousser les détails à plus tard
- Organiser et simplifier les classes en utilisant l'héritage

## Contenu du diagramme
### Classe
__Rappel :__ _Une classe est la description formelle d'un ensemble d'objets ayant une sémantique et des caractéristiques communes._

Dans le diagramme, on a trois compartiments différents : le __nom__, les __attributs__ et les __opérations__.

#### Le nom
Le nom doit être significatif et évoquer le concept décrit par la classe

#### Les attributs
De la forme `visibilité (+, #, -) nomAttribut : Type`.

On indique un attribut dérivé (qu'on peut calculer) par un `/` après la visibilité.

Les attributs de classe sont propres à la classe et non à l'objet. On les souligne.

Visibilité : private (-), public (+), protected (#)

### Associations
Les associations représentent des relations structurelles entre classes et objets.

On peut définir le rôle de la classe au sein d'une association. Les rôles agissent comme une propriété (un attribut). Ils peuvent donc avoir une visibilité.