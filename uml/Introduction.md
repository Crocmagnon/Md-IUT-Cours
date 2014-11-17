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

### Cycle de vie en cascade
- Étude des besoins
- Analyse
- Conception
- Code
- Test
- Déploiement

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
