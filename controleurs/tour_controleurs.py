import random
from tinydb import TinyDB, Query


class Tour:

    def __init__(self):
        self.db = TinyDB('database/database_joueurs.json')
        self.dbclassement = TinyDB('database/dbclassement.json')

    #on génère le tour 1 automatiquement
    def generate_tour(self):
        result = self.db.all()
        round = 4
        groupe1 = result[:4]
        groupe2 = result[4:]
        matchs = []
    
        for i in range(round):
            print(i)
            groupe1[i].points = random.randint(0, 20)
            
            groupe2[i].points = random.randint(0, 20)
        if groupe1[i].points > groupe2[i].points:
            groupe1[i]["score"] += 1
            print(groupe1[i]["nom"] + " gagne")
        elif groupe2[i].points > groupe1[i].points:
            groupe2[i]["score"] += 1
            print(groupe2[i]["nom"] + " gagne")
        else:
            groupe1[i]["score"] += 0.5
            groupe2[i]["score"] += 0.5

        match = ((groupe1[i]["nom"], groupe2[i]["nom"]), (groupe1[i]["score"], groupe2[i]["score"]))
        matchs.append(match)

        for match in matchs:
            print(match)

        playerslists = groupe1 + groupe2
        playerslists_ordering = sorted(playerslists, key=lambda x: x["score"], reverse=True)

        # - # ------------------ ROUND 1 -----------------
        matchs = []
        #génération des rounds suivants
        for i in range(round):
            groupe1[i].points = random.randint(0, 20)
            groupe2[i].points = random.randint(0, 20)
            if groupe1[i].points > groupe2[i].points:
                groupe1[i]["score"] += 1
                print(groupe1[i]["nom"] + " gagne")
            elif groupe2[i].points > groupe1[i].points:
                groupe2[i]["score"] += 1
                print(groupe2[i]["nom"] + " gagne")
            else:
                groupe1[i]["score"] += 0.5
                groupe2[i]["score"] += 0.5
 
            match = ((groupe1[i]["nom"], groupe2[i]["nom"]), (groupe1[i]["score"], groupe2[i]["score"]))
            matchs.append(match)
      
        for match in matchs:
            print(match)

        #gestion du tour par tour    
        playerslists = groupe1 + groupe2
        playerslists_ordering = sorted(playerslists, key=lambda x: x["score"], reverse=True)   
        compteur = 1     
        reponse = input("1.Oui\n2.Non\n")
            
        if reponse == "1":
            reponse_utilisateur = True
        if reponse == "2": 
            reponse_utilisateur = False
        print(reponse_utilisateur)

        while compteur < 9 and reponse_utilisateur == True: 
            print(f" ------------------ ROUND {compteur+1} -----------------")
            current_round = []
            playerslists_ordering = sorted(playerslists, key=lambda x: x["score"], reverse=True)
            print(playerslists_ordering)
            for i in range(0, 8):
                p1 = playerslists_ordering[i]["nom"]
                for j in range(i+1, 8):
                    p2 = playerslists_ordering[j]["nom"]
                    print(p1, p2)
                    match = ((playerslists_ordering[i]["nom"], playerslists_ordering[j]["nom"]), (playerslists_ordering[i]["score"], playerslists_ordering[j]["score"]))
                    if self.check_match(p1, p2, matchs) == False:  
                        if self.check_player(p1, p2, current_round) == False:
                            current_round.append(match)
                            matchs.append(match)
                            self.update_score(playerslists_ordering[i], playerslists_ordering[j])                  
                            break                        
            print(matchs)
            compteur += 1
            if len(current_round) == 0:
                print("plus de matchs possibles")

            match_sauvegarde = self.serialize_matchs(matchs)
            database = self.dbclassement
            database.insert(match_sauvegarde)
            reponse = input("1.Oui\n2.Non\n")

            if reponse == "1":
                reponse_utilisateur = True
            if reponse == "2":
                reponse_utilisateur = False
            print(reponse_utilisateur)

    def check_match(self, p1, p2, matchs):
        for item in matchs:
            if (p1 == item[0][0] and p2 == item[0][1]) or (p1 == item[0][1] and p2 == item[0][0]):
                return True
        return False

    def check_player(self, p1, p2, match_round2):
        for item in match_round2:
            if (p1 == item[0][0] or p1 == item[0][1]) or (p2 == item[0][0] or p2 == item[0][1]):
                return True
        return False

    #update du score des joueurs
    def update_score(self, p1, p2):
        Joueur = Query()
        liste_joueurs = self.db.table("_default")
        score_p1 = int(float(input("Entrez le score du joueur {}".format(p1["nom"]))))

        if score_p1 == 1:
            p1["score"] += 1
            p2["score"] += 0
        elif score_p1 == 0:
            p1["score"] += 0
            p2["score"] += 1
        else:
            p1["score"] += 0.5
            p2["score"] += 0.5
        liste_joueurs.update({'score': p1["score"]}, Joueur.nom == p1["nom"])
        liste_joueurs.update({'score': p2["score"]}, Joueur.nom == p2["nom"])

    def serialize_matchs(self, match):
        resultat = {"match": match}
        return resultat
