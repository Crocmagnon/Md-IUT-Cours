# Algo avancée - Introduction
## Présentation prof
M. KHEDDOUCI Hamamache, 2e étage  
hamamache.kheddouci@univ-lyon1.fr

## Présentation cours
On va parler des structures de données (SDD).

Deux mots-clé :  
__Structure__ & __Données__: On doit trouver une structuration des données (comment les stocker) pour le client. C'est important de structurer les données pour obtenir des algos plus efficaces. En effet, les algos sont plus efficaces s'ils fonctionnent sur des données structurées plutôt que sur des données brutes.

## Contenu
- Listes simples, bidirectionnelles, circulaires
- Piles
- Files
- Arbres
- Complexité des algorithmes

## Problématique
Les tableaux ont une taille fixe. Ce n'est pas intéressant pour des volumes variables de données. En effet, l'espace mémoire est une ressource. Et il ne faut pas gaspiller les ressources.  
L'idée est de trouver une manière dynamique de demander de l'espace mémoire en fonction des données à stocker. Le problème est qu'on a plus de lien entre les cases. Il faut alors également réserver de l'espace dans la "case" pour le chaînage (quel est l'élément suivant).  
Cette structure de données correspond aux listes.

L'avantage des listes est son dynamisme. Son inconvénient est la lenteur de l'accès aux données (on est obligés de passer par la tête de la liste puis par toutes les cases suivantes pour accéder à une valeur).

## Exercice
Écrire un algo de création de LLC (Liste Linéaire Chaînée) avec des valeurs saisies par l'utilisateur.