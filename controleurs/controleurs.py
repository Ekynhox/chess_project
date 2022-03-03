from tinydb import TinyDB
from vue.view import Menu
from controleurs.tour_controleurs import Tour
from modeles.tournois import Tournoi
import json

db = TinyDB('database/database_joueurs.json')
dbclassement = TinyDB('database/dbclassement.json')


class Controleur:
    def __init__(self):
        self.view = Menu()
        self.users = []
        self.tournois = Tournoi()

    def run(self):
        choice = self.view.display_menu()
        if choice in range(1, 9):
            if choice == 1:
                self.tournois.save_tournoi()
                return self.run()
            elif choice == 2:
                self.create_user()
                return self.run()
            elif choice == 3:
                self.display_user_list()
                return self.run()
            elif choice == 4:
                db.drop_tables()
                return self.run()
            elif choice == 5:
                self.create_tour()
                return self.run()
            elif choice == 6:
                self.classement()
                return self.run
            elif choice == 7:
                self.tournois.afficher_tournoi()
                return self.run()
            elif choice == 8:
                self.tournois.supprimer_tournois()
                return self.run()

        else:
            self.view.display_message("""Choix incorrect,
                merci de faire un choix entre 1 et 6.""")
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
        tournoidb = {}
        with open('database/dbtournoi.json') as json_file:
            data = json.load(json_file)
            print(data)
            tournoidb = data
        if not tournoidb:
            print("Veuillez créer un tournoi.")
            self.run()
        else:
            tour = Tour()
            tour.generate_tour()

    # création du classement
    def classement(self):
        liste_joueurs = db.table("_default")
        result = liste_joueurs.all()
        result_sorted = sorted(result, key=lambda d: d['score'], reverse=True)
        print(result_sorted)
        pass
