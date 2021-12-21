import random

class Player:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.points = Player.random()
        self.score = score

    def __str__(self):
        return f"{self.name}"
    def random():
        return random.randint(0, 20)
    def saveplayer(self):
        pass

class Match:

    def __init__(self, manche, resultat, matchs):
        self.manche = ""
        self.resultat = 1
        self.joueurs = ""

    def check_match(self, p1, p2, matchs):
        for item in matchs:
            if (p1 == item[0][0] and p2 == item[0][1]) or (p1 == item[0][1] and p2 == item[0][0]):
                return True
        return False
        
    def check_player(self, p1, p2, manche):    
        for item in manche: 
            if (p1 == item[0][0] or p1 == item[0][1]) or (p2 == item[0][0] or p2 == item[0][1]):  
                return True           
        return False



class Generate_Round: 
    def __init__(self, score):
        self.score = 1


    def round_possible(self, matchs):
        #if tous les joueurs se sont affrontés dans l'historique des matchs sinon, création de round

        
        return False
    # générer les rounds : tant que les joueurs se sont affronter on génère des rounds dans la limite de 8 round