from tinydb import TinyDB, Query, where
from view import Menu
from tour_controleurs import Tour

db = TinyDB('database.json')


class Controleur:
    def __init__(self):
        self.view = Menu()
        self.users = []    

    def run(self):       
        choice = self.view.display_menu()
        if choice in range(1, 5):
            if choice == 1:
                return self.create_user()
            elif choice == 2:
                return self.display_user_list()
            elif choice == 3:     
                db.drop_tables()
                return self.run()
            elif choice == 4:
                return self.create_tour()
                

        else:
            self.view.display_message("Choix incorrect, merci de faire un choix entre 1 et 3.")
            return self.run()
    
    def create_user(self):

        nom = self.view.get_user_input("Entrez le nom de l'utilisateur.\n")
        age = self.view.get_user_input("Entrez l'âge de l'utilisateur.\n")
        score = self.view.get_user_input("Entrez le score de l'utilisateur.\n")
        user = self.serialize_user(nom, age, int(score))
        db.insert(user)
        self.users.append(user)
        self.view.display_message("Utilisateur créé avec succès.")
        self.run()
            
        
    def display_user_list(self):
        for item in db:
            print(item)
        self.view.display_message("Liste affichée avec succès.")
        self.run()

    def serialize_user(self, nom, age, score):
        user = {
            "nom": nom,
            "age": age,
            "score": score
        }
        return user

    def create_tour(self):
        tour = Tour()
        tour.generate_tour()




# class Controleur_joueur:
#     pass

# class Controleur_match:
#     pass

# class Constroleur_round:
#     pass

# class Controleur_resultat():
#     # resultat = input("Entrez le résultat")
#     # if resultat == 1:
#     #     print("P1 a gagné")
#     # elif resultat == 0:
#     #     print("P1 a perdu")
#     # elif resultat == 0.5:
#     #     print("Egalité")

# class Controleur_menu():
#     pass


# créer méthode pour créer tour, quand on créée un tour il faut enregistrer les matchs dans la base de données au fur et à mesure
# mettre la génération de tour sous forme manuelle (pas prio)
# enregistrer tous les matchs avec le résultat
# méthode créer joueur/afficher liste des joueurs 
# plusieurs class (controleur_joueur, controleur_match, controleur_round etc)
#modèle pour les joueurs/matchs
#vue pour les joueurs/matchs 

#controleur sont des actions en fonction du choix de l'utilisateur quand il va effectuer une action, ça va afficher un menu 
#stocker l'input en variable