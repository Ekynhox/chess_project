class Menu:

    def __init__(self):
        pass

    def display_menu(self):
        return int(input("""1. Créer un tournoi\n2. Ajouter un nouveau joueur \n3. Afficher la liste des joueurs\n4. Supprimer tout les joueurs
5. Générer les tours\n6. Afficher le classement\n7. Afficher la liste des tournois\n8. Supprimer tout les tournois\n"""))

    def display_message(self, message):
        print(message)

    def get_user_input(self, message):
        return input(message)
