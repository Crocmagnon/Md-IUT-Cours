def miroir():
    pile = creer_pile()
    car = input("Saisir un caractère : ")
    while car <= 'z' and car >= 'a' or car <= 'Z' and car >= 'A':
        empile(pile, car)
        car = input("Saisir un caractère ")

    while not pile_vide(pile):
    	print(sommet(pile), end="")
    	depile(pile)
    print()

def separate_car():
	chaine = input("Saisir une chaine : ")
	for car in chaine:
		print(car)