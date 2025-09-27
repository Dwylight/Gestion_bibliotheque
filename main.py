import library

mythologie = library.Book("Poséidon", "Jean Martin", True)
romance = library.Book("Sens contraires", "Céline Gourmet", True)
poesie = library.Book("Les Misérables", "Victor Hugo", True)
histoire = library.Book("L'empire du Mali", "Joseph Kizerbo",True)

titres = {
    "Poséidon": mythologie,
    "Sens contraires": romance,
    "Les Misérables": poesie,
    "L'empire du Mali": histoire
}

auteurs = {
     "Jean Martin": mythologie,
     "Céline Gourmet": romance,
     "Victor Hugo":poesie,
     "Joseph Kizerbo": histoire
}

collection_savoir = library.Library()
collection_savoir.collection = [mythologie, romance, poesie, histoire]

print("*********************\n"
"BIBLIOTEQUE LE SAVOIR\n"
"*********************\n")
while True:
    print("\n---MENU---\n" 
    "1. Ajouter un livre\n" 
    "2. Rechercher un livre\n"
    "3. Emprunter un livre\n" 
    "4. Rendre un livre\n" 
    "5. Quitter\n")
    choix = input("Quel est votre choix?: ")

    if choix == "1":
        titre = input("Entrez le titre de l'oeuvre: ")
        auteur = input("Donner le nom de l'auteur: ")
        livre = library.Book(titre, auteur, True)
        collection_savoir.ajouter_livre(livre)
        titres[titre] = livre
        auteurs[auteur] = livre     
    elif choix == "2":
        livre_a_rechercher = input("Donnez l'intitulé du livre ou son auteur: ")
        if livre_a_rechercher in titres:
            livre = titres[livre_a_rechercher]
            collection_savoir.rechercher_livre(livre)
        elif livre_a_rechercher in auteurs:
            livre = auteurs[livre_a_rechercher]
            collection_savoir.rechercher_livre(livre)
        else:
            print("Nous sommes désolés, ce livre ne figure pas dans notre collection")
    elif choix == "3":
        titre_a_emprunter = input("Donnez l'intitulé du livre: ")
        if titre_a_emprunter in titres:
            livre_a_emprunter = titres[titre_a_emprunter]
            collection_savoir.emprunter_livre(livre_a_emprunter)
        else:
            print("Nous sommes désolés, ce livre ne figure pas dans notre collection")
    
    elif choix == "4":
        titre_a_rendre = input("Donnez le titre du livre à rendre: ")
        if titre_a_rendre in titres:
            livre_a_rendre = titres[titre_a_rendre]
            collection_savoir.rendre_un_livre(livre_a_rendre)
        else:
            print("Ce livre ne figure pas dans notre collection")
    elif choix == "5":
        print("Merci d'être passé à la bibliothèque le Savoir, A bientôt!")
        break
    else:
        print("Veuillez entrer un numéro valide!")
        

        #En attente de validation
        

    
