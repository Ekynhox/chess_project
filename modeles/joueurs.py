from tinydb import TinyDB, Query

class Joueurs:
    def __init__(self, db, dbclassement):
        self.db = TinyDB('database/database_joueurs.json') #db 
        self.dbclassement =  TinyDB('database/dbclassement.json') #dbclassement

    def save_joueurs(self, joueur):
        self.db.insert(joueur)

    def serialize_user(self, nom, age, score):
        user = {
            "nom": nom,
            "age": age,
            "score": score
        }
        return user

    def get_all_joueurs(self):
        return self.db.all()

    def get_classement(self):
        return self.db.all()
    def delete_all_joueurs(self):
        return self.db.drop_tables()

    def update_score_joueur(self, p1, p2):
        Joueur = Query()
        liste_joueurs = self.db.table("_default")
        liste_joueurs.update({'score': p1["score"]}, Joueur.nom == p1["nom"])
        liste_joueurs.update({'score': p2["score"]}, Joueur.nom == p2["nom"])