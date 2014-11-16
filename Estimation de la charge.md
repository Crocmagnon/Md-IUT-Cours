# Méthodes d'estimation de la charge
## Méthode EXPERT (ou DELPHI)
On fait appel à des experts pour donner une estimation sur le sujet.

Experts | Applications jugées comparables en charge | Charges correspondantes  | 1ères estimations 
--------|-------------------------------------------|--------------------------|--------------------
A       | D04                               | 9 m-h  | [8;13] -> 10&nbsp;m-h
        | K67                               | 13 m-h |
        | RESA                              | 8 m-h  |
B       | IA55                              | 6 m-h  | [5;6] -> 8&nbsp;m-h
        | SCI8                              | 5 m-h  |
        | BIB1                              | 6 m-h  |
C       | APP                               | 14 m-h | [14;21] -> 14&nbsp;m-h
        | ASS8                              | 21 m-h |
D       | K67                               | 13 m-h | [13;21] -> 15&nbsp;m-h
        | APP                               | 14 m-h |
        | ASS8                              | 21 m-h |

On s'entendra peut-être sur __12 m-h__

## Méthode par répartition proportionnelle
On utilise la méthode MERISE qui estime qu'il y a des étapes par lesquelles il faut passer. En connaissant les proportions de répartition, on peut déduire du temps de la première phase, la durée de tout le projet. 

### Répartition
1. Étude préalable __(10%)__
    - Observation, on rencontre le client __(1/3)__ :
        - On complète la rédaction du CdC qui devient un CdC de réalisation
          - DRH         :   2 j
          - DG          : 1,5 j
          - DIVERS      :   3 j
          - Appro + Log : 0,5 j
        - __Total       :   7 j__
    - Conception - Organisation
    - Appréciation
2. Étude détaillée
3. Réalisation

### Estimation
$7\textrm{ j-h} * 3 = 21\textrm{ j-h}$  
Projet estimé à  $21\textrm{ j-h} * 10 = 210\textrm{ j-h}$  
Soit __~11 m-h de 20 jours ouvrés__

## Méthode COCOMO
$$\textrm{Charge brute} = a * \textrm{KISL}^b$$

`KISL` = Kilo Instruction Source Livrée

$$\textrm{Délai} = c * \textrm{Charge brute}^d$$  

`a`, `b`, `c` et `d` sont à choisir par l'utilisateur de la méthode.  

$$\textrm{Charge nette} = \textrm{Charge brute} * \Pi(\textrm{Coeffs de niv. d'exigence})$$

Délai :

- Techniquement possible
- Commercialement acceptable

Ici : 

$$\textrm{Charge} = 2,4 * 5^{1,05} = 13\textrm{ m-h}$$
$$\textrm{Délai} = 2,5 * 13^{0,38} = 7\textrm{ mois}$$

## Méthode DIEBOLD
$$\textrm{Charge (en j-h)} = \textrm{KISL} * \textrm{Complexité} * \textrm{Savoir-faire} * \textrm{Connaissance}$$  
$\textrm{Complexité} \in [10;40]$  
$\textrm{Savoir faire} \in [0,65;2]$  
$\textrm{Connaissance} \in [1;2]$  
$$\textrm{Charge} = 5 * \frac{40 * 8 + 25 * 19 + 10 * 10}{37} * 1 * 1,5 = 180 \textrm{ j-h}$$  

## Méthode analytique
On aborde cette méthode quand on a signé avec le client.  
Il faut entrer dans le détail des tâches.

__Plusieurs grandes étapes :__

- Étude préalable -> $10%$ du projet -> 20,5 j-h
- Étude détaillée -> $\frac{1}{2}$ Réalisation -> 61,5
- Réalisation -> 123 j-h (voir étude de cas)
  - Étude technique
  - Programmation
  - Jeux d'essais
  - Tests & corrections

$\textrm{Estimation projet} = \frac{61,5+123}{0,9} = 205$

Dans l'étape de programmation on va rechercher des tâches standards (voir tableau page 30).  
On arrive alors à un certain temps en j-h pour la programmation qui constitue la base. On prend un certain pourcentage de cette base pour chacune des autres étapes de la réalisation.

## Méthode des points de fonction
### Principe
Il faut prévoir d'autant plus de temps pour réaliser un projet :

### Qu'on doit intégrer un grand nombre d'informations
5 types de composants fonctionnels :

* GD Internes = Entités internes à créer pour les besoins du projet
  * Véhicules __F__
  * Marque-Modèle __F__
  * Autorisation habituelle __F__
  * Autorisation exceptionnelle __F__
* GD Externes = Entités déjà existantes dans le SI du client et sur lesquelles on s'appuie
  * Employés __M__
  * Bâtiments __M__
  * Parkings __F__
* ENTrées
  * 6 (4 : une pour chaque GDI, 1 pour qu'un employé demande une autorisation exceptionnelle et 1 pour insérer les N° de véhicules dans la table employés) : 5 __F__ & 1 __M__
* SORties
  * 10 __F__
* INTerrogations
  * 18 : 13 __M__ & 5 __D__

### Que les contraintes d'exploitation sont fortes
$$\textrm{DIT} = \sum{\textrm{points de niveau de difficulté d'exploitation}}$$
$$\textrm{DIT} \leq 70$$
$$\textrm{FA} = 0,65 + \frac{\textrm{DIT}}{100} = 0,9$$
$$\textrm{PFA} = \textrm{PFB} * \textrm{FA} = 112 * 0,9 \simeq 100 \textrm{points ajustés}$$

`FA` = Fonction d'ajustement
`PFB` = Points de Fonction Bruts (ceux calculés avant)
`PFA` = Points de Fonction Ajustés

Au final cette méthode ne permet pas de découper le travail entre collaborateurs