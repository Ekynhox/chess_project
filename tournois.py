from tinydb import TinyDB
from view import Menu


dbtournoi = TinyDB("dbtournoi.json")

class Tournoi:

    def __init__(self):
        self.view = Menu()
        self.tournois = []


    def save_tournoi(self):
        nom = self.view.get_user_input("Entrez le nom du tournoi.\n")
        date = self.view.get_user_input("Entrez la date du tournoi : xx/xx/xxxx.\n")
        lieu = self.view.get_user_input("Entrez le lieu où se déroule le tournoi.\n")
        tournoi = self.serialize_tournoi(nom, date, lieu)
        dbtournoi.insert(tournoi)

    def serialize_tournoi(self, nom, date, lieu):
        user = {
            "nom": nom,
            "date": date,
            "lieu": lieu
        }
        return user

    def afficher_tournoi(self):
        for item in dbtournoi:
            print(item)
    
    def supprimer_tournois(self):
        dbtournoi.drop_tables()


# vérifie avec flake8 le pep 8, et créer un dossier 
#qui contient le view et modele, et en dehors du dossier, le main.py, faire le fichier readme.md