from tinydb import TinyDB
from vue.view import ClassementView
from vue.view import Menu, JoueursView, TournoiView
from controleurs.tour_controleurs import Tour
from modeles.tournois import Tournoi
from modeles.joueurs import Joueurs
import json

db = TinyDB('database/database_joueurs.json')
dbclassement = TinyDB('database/dbclassement.json')


class Controleur:
    def __init__(self):
        self.view = Menu()
        self.view_joueur = JoueursView()
        self.view_tournoi = TournoiView()
        self.view_classement = ClassementView()
        self.users = []
        self.tournois = Tournoi()
        self.joueurs = Joueurs(db, dbclassement)
        self.tour = Tour()

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
                self.joueurs.delete_all_joueurs()
                return self.run()
            elif choice == 5:
                self.create_tour()
                return self.run()
            elif choice == 6:
                self.display_classement()
                return self.run
            elif choice == 7:
                self.display_tournoi()
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
        user = self.joueurs.serialize_user(nom, age, int(score))
        self.joueurs.save_joueurs(user)
        self.users.append(user)
        self.view.display_message("Utilisateur créé avec succès.")
        self.run()

    def display_user_list(self):
        joueurs_list = self.joueurs.get_all_joueurs()
        self.view_joueur.display_users(joueurs_list)
        self.run()
    
    def display_tournoi(self):
        tournoi_list = self.tournois.get_all_tournoi()
        self.view_tournoi.display_tournoi(tournoi_list)
        self.run()
    
    def display_classement(self):
        classement = self.joueurs.get_classement()
        self.view_classement.display_classement(classement)
        self.run()
        

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
            self.tour.generate_tour()

    # création du classement
    def classement(self):
        result = self.joueurs.get_all_joueurs()
        result_sorted = sorted(result, key=lambda d: d['score'], reverse=True)
        print(result_sorted)
        pass
