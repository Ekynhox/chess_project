from tinydb import TinyDB
from vue.view import TournoiView
from vue.view import Menu


dbtournoi = TinyDB("database/dbtournoi.json")
db = TinyDB('database/database_joueurs.json')
dbclassement = TinyDB('database/dbclassement.json')

class Tournoi:

    def __init__(self):
        self.view = Menu()
        self.view_tournoi = TournoiView()
        self.tournois = []
        
    def save_tournoi(self):
        nom = self.view_tournoi.display_tournoi_nom()
        date = self.view_tournoi.display_tournoi_date()
        lieu = self.view_tournoi.display_tournoi_lieu()
        tournoi = self.serialize_tournoi(nom, date, lieu)
        dbtournoi.insert(tournoi)

    def serialize_tournoi(self, nom, date, lieu):
        user = {
            "nom": nom,
            "date": date,
            "lieu": lieu
        }
        return user

    def get_all_tournoi(self):
        return dbtournoi.all()

    def supprimer_tournois(self):
        dbtournoi.drop_tables()

        #refaire la séparation des couches MVC, et améliorer l'affichage des données en console