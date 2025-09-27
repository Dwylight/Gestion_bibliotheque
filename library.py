class Book:
    def __init__(self, titre, auteur, disponible = True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible
    def __str__(self):
        return (
            f"- Titre : {self.titre}\n"
            f"- Auteur : {self.auteur}"
        )
            


class Library:
    def __init__(self):
        self.collection = []

    def ajouter_livre(self, livre_a_ajouter):
        self.collection.append(livre_a_ajouter)
        print(f"le livre {livre_a_ajouter.titre} a été ajouté à la collection")

    def emprunter_livre(self, livre_a_emprunter):
        if livre_a_emprunter.disponible:
            print(f"Vous avez emprunté le livre {livre_a_emprunter.titre}")
            livre_a_emprunter.disponible = False
        else:
            print(f"Le livre {livre_a_emprunter.titre} n'est pas disponible")

    def rendre_un_livre(self, livre_a_rendre):
        if not livre_a_rendre.disponible:
            print(f"Vous avez rendu le livre {livre_a_rendre.titre}")
            livre_a_rendre.disponible = True
        else:
            print("Vous n'aviez pas emprunté ce livre dans notre collection.")
            
    def rechercher_livre(self, livre_a_rechercher):
        print(livre_a_rechercher)


    
    