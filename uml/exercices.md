# Exercices
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