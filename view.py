class Menu:
    def __init__(self):
        pass
    def display_menu(self):
        return int(input("1. Ajouter un nouveau joueur \n2. Afficher la liste des joueurs\n3. Supprimer tout les joueurs\n4. Générer les tours\n"))
    def display_message(self, message):
        print(message)
    def get_user_input(self, message):

        return input(message)

