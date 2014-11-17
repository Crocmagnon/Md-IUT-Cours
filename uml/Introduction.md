# Introduction à UML
## Différentes catégories de logiciels

- Logiciel embarqué
    Intégré dans des composants matériels (GPS, tel., MP3, console de jeux, ...)
- Logiciel temps réel
    Interagit avec l'extérieur, évolue dans le temps (conduite automatique, ...)
- Logiciel d'entreprise
    Comptabilité, commandes
- Logiciel scientifique
    Calcul scientifique (stats, IA, calcul financier, prévision, météo, nucléaire, ...)
- Logiciel Web
    Création de sites/pages, blogs, moteurs de recherche

## Contexte général
Il faut traiter l'information nécessaire aux entreprises.
Le SI regroupe l'ensemble des ressources (personnel, matériel, logiciel). Il se construit autour de __processus métier__ et ses interactions.

Les différents acteurs sont :

- La DSI
- La MOA (donneur d'ordre)
- La MOE (exécutant, réalisateur)
- Les utilisateurs

Il faut faire le lien entre la __vision métier__ (organisation et ses processus), la __vision fonctionnelle__ (le SI), et la __vision informatique__ (applications, technologie de l'information).

## Modélisation
### Pourquoi modéliser
On modélise pour mieux comprendre le système, maîtriser sa complexité et assurer la cohérence, préciser le problème donné et son champ d'application.

Un modèle est un __langage commun__, un outil de communication entre les acteurs. C'est une représentation simplifiée de la réalité.

Un modèle permet de réduire la complexité d'un phénomène en éliminant les détails qui n'influencent pas sa compréhension.

La réalisation d'un SI impose la création de modèles successifs

- Chaque modèle représente le système à un certain niveau d'abstraction
    + Les premiers modèles représentent le système dans sa globalité
    + Les derniers permettent la réalisation technique

## Modéliser avec UML
### UML, c'est quoi ?
C'est une notation, un formalisme permettant la modélisation.

C'est un langage de modélisation graphique et textuel conçu pour

- Visualiser
- Spécifier
- Construire
- Documenter

Ce n'est __pas__ une méthodologie de développement.  
Une méthode de dev définit une démarche reproductible pour obtenir des résultats fiables. Elle définit un cycle de dev et des techniques à utiliser.

### Vers un langage unifié de modélisation orientée objet
- Fondements pour spécifier, construire et décrire les différentes vues d'un système logiciel, les différents niveaux d'abstraction
- Syntaxe et sémantique précises
- Limiter les ambiguïtés
- Faciliter communication, documenter
- Notation graphique
- ...

UML date de 1996.

## Méthodes de développement.
### Cycle de vie en cascade
- Étude des besoins
- Analyse : On commence à construire les modèles
- Conception : On définit l'architecture du système, on affine les modèles
- Code : On traduit le modèle en code
- Test : Vérification des exigences
- Déploiement : On déploie chez le client

=> Vérification (tests) trop tardive

### Processus en V
Mise en relation des phases en amont avec les phases de tests en aval.
Spécifications => Validation
Conception prélim => Intégration
Conception détaillée => Tests unitaires
Code

### Méthodes agiles
- Adaptation au changement plus que suivi d'un plan
- Intégration du client au processus de développement : l'utilisateur final fait partie de l'équipe.
- Acceptation du changement dans les besoins
- Travail d'équipe

Démarche incrémentale : Projet évolutif, on procède par incrément et prototypage.  
On identifie les besoins, on en sélectionne pour le sprint (on code vite, en général 2 semaines), et on recommence pour itérer jusqu'au produit final.

## Orienté objet
Paradigme consistant à modéliser par la définition et l'interaction de briques appelées objets.  
Un objet représente un concept, une idée, ou toute entité du monde physique, comme une voiture, une personne.

### Classe
Regroupe les entités qui se ressemblent dans leur __description__ (attributs) et __comportement__ (opérations).

### Objet
Un objet est une entité aux frontières définies, possédant une entité et encapsulant un état et un comportement.

__Un objet est une instance d'une classe__.

    Objet = État + Identité + Comportement

### Héritage
Réutilisation d'une classe pour en créer une nouvelle : généralisation/spécialisation.

On __factorise les éléments communs__ d'un ensemble de classe dans une classe plus générale appelée __super-classe__.  
Les classes plus spécialisées sont des __sous-classes__.

La généralisation correspond au lien sémantique "est un" (par ex. : Un Étudiant est une Personne).

### Association
Une relation sémantique entre classes.  
Représente l'ensemble des liens entre les objets des classes qui participent à l'association.

### Lien
Une connexion entre objets, une instance d'une association.

Ex :  
Pays 'a pour capitale' Ville => Association  
France 'a pour capitale' Paris => Lien

### Encapsulation
Principe de conception qui consiste à protéger le coeur du système de tout accès intempestif venant de l'extérieur. Il faut limiter l'accès aux informations internes à une classe.

Les valeurs des attributs d'un objet ne peuvent pas être manipulées directement par les autres objets.  
Seules les opérations sont accessibles.


