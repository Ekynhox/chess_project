class Menu:

    def __init__(self):
        pass

    def display_menu(self):
        return int(input("""1. Créer un tournoi\n2. Ajouter un nouveau joueur \n
3. Afficher la liste des joueurs\n4. Supprimer tout les joueurs
5. Générer les tours\n6. Afficher le classement\n
7. Afficher la liste des tournois\n8. Supprimer tout les tournois\n"""))

    def display_message(self, message):
        print(message)

    def get_user_input(self, message):
        return input(message)

class TournoiView:
    def __init__(self):
        return
        
    def display_tournoi_nom(self):
        return input("Entrez le nom du tournoi.\n")

    def display_tournoi_date(self):
        return input("Entrez la date du tournoi : xx/xx/xxxx. \n")
    
    def display_tournoi_lieu(self):
        return input("Entrez le lieu où se déroule le tournoi. \n")
    
    def display_score_joueur(self, p1):
        return int(float(input("""
        Entrez le score du joueur {}""".format(p1["nom"]))))

    def display_tournoi(self, tournois):
        for item in tournois:
            print("Nom: ", item["nom"], '| Date: ', item["date"], "| Lieu: ", item["lieu"])
class JoueursView:
    
    def display_users(self, users):
        for item in users:
            print("Nom:", item["nom"], '| Score: ', item["score"], "| Age: ", item["age"])

class ClassementView :
    
    def display_classement(self, classement):
        classement_sorted = sorted(classement, key=lambda d: d['score'], reverse=True)
        for item in classement_sorted:
            print("Nom:", item["nom"], "| Age: ", item["age"], '| Score: ', item["score"])
