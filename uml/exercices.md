# Exercices TD1
## Exercice 1
On souhaite modéliser le fonctionnement et l'usage d'un lecteur de DVD.

### Question a
Les entités impliquées dans le fonctionnement d'un lecteur de DVD sont : Le lecteur DVD, le DVD, l'usager, la télévision.

### Question b
Les fonctionnalités principales d'un lecteur DVD sont : la lecture d'un DVD, l'affichage sur un écran externe.

### Questions c et d
Lancer la lecture du DVD, mettre en pause, arrêter la lecture, avance/recul rapide, saut de chapitres, accès au menu, affichage de sous-titres, changement de piste audio, éjecter, ...

### Question e
Retour d'erreur, refuse la lecture

### Question f
Identification de la zone, décodage, affichage, gestion d'erreur

## Exercice 2
Scénario

### Questions a et b
- Patient
    + Nom
    + Prénom
    + Âge
    + Adresse
    + N° Sécu
- Dossier médical
- Consultation
    + Date
    + Heure
    + Présence patient
    + Prescription
    + Hospitalisation
- Médecin
- Infirmière
- Opératrice
- Examen
    + Intitulé
    + Date
    + Heure
- Lit

### Question c
Créer un dossier médical, un patient, une consultation.  
Réalisation examen

### Question d
Obtenir un rendez-vous, valider une consultation, admission patient

## Exercice 3
### Questions a et d
- Client
- Chéquier
    + Débiter
    + Refuser
- Chèque
- Compte bancaire
    + Débiter
    + Créditer
    + Clôturer
    + Consulter solde
    + Consulter historique
- GAB
    + Retirer de l'argent
    + Consulter solde
    + Imprimer ticket
    + Afficher les informations
- Lecteur de carte
- Imprimante
- Clavier
- Écran
- Clavier
- Touche

### Question b
- Client possède Chéquier
- Chèque est associé à Compte
- Client signe un Chèque
- Compte est associé à Client
- Chéquier est composé de Chèques
- Clavier est composé de Touches
- GAB est composé d'un Lecteure de carte, d'une imprimante, d'un clavier et d'un écran
- Un Clavier est composé d'un ensemble de Touches

### Question c
On passe parce que c'est un peu toujours les mêmes choses.

### Question e
- Entité = classe
- Relation = Association
- Propriété = Attribut
- Action = Méthode

# Exercices TD2
## Questions de cours
__Classe__ :

- Entité qui a un sens propre dans le domaine observé.
- Description d'un ensemble d'objets similaires ayant des caractéristiques (propriétés) et de relations en commun.
- Définition des propriétés et du comportement.
- Ex : Personne, Voiture

__Objet__ :

- Une entité aux frontières bien définies, possédant une identité et encapsulant un état et un comportement.
- Enseignant "Annie"

__Attribut__ : Propriété d'une classe, dont la valeur peut varier pour chaque objet.

__Méthode__ : Mise en œuvre d'une opération dans un objet.

__Tout objet possède un état, une identité et un comportement.__ :

- Un objet est identifié de manière unique par son identité, indépendemment de son état.
- État : ensemble de valeurs associées aux attributs de l'objet à un instant
- Comportement : décrit par ses opérations, définit les actions et réactions d'un objet.

__Héritage__ : Réutilisation d'une classe pour la création d'une nouvelle classe à travers la spécialisation de la première dans la seconde.  
L'héritage permet de factoriser les éléments communs d'un ensemble de classes dans une super-classe commune à toutes les autres classes.

__Association__ : Une relation sémantique entre classes. Par exemple : Un enseignant _est responsable_ d'un cours.

__Lien__ : Instance d'une association. Par ex : L'enseignante "Marie-Aude" est responsable du cours UML.

__Encapsulation__ : Les valeurs des attributs ne sont pas accessibles en dehors de l'objet. Améliore la sécurité, le contrôle des données et prévient des accès non autorisés.

## Exercice 1
### Question 1
- Forme (couleur, orientation)
    + 1D (longueur)
    + 2D (surface)
        * Polygône (nb_cotes)
            - Parallélogramme (longueur, largeur)
                + Rectangle
                + Losange (longueur_cote)
            - Triangle (long1, long2, long3, angle1, angle2, angle3)
            - Étoile (nb_branches, long_branches)
        * Flèche (direction, courbe)
        * Smiley
    + 3D (volume)
        * Parallélépipède (longueur, largeur, profondeur)


