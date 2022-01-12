import random
import json
from modeles import Player
from tinydb import TinyDB, Query

class Tour:

    def __init__(self):
        self.db = TinyDB('database.json')
        
    def generate_tour(self):
        result = self.db.all()
        round = 4
        nombre_de_joueurs = 8
        groupe1 = result[:4]
        groupe2 = result[4:]
        matchs = []

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

        playerslists = groupe1 + groupe2
        playerslists_ordering = sorted(playerslists, key=lambda x: x["score"], reverse=True)
        next = True


        # - # ------------------ ROUND 1 -----------------
        matchs = []

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
            
        playerslists = groupe1 + groupe2
        playerslists_ordering = sorted(playerslists, key=lambda x: x["score"], reverse=True)    
        
        compteur = 1
        while compteur < 9: 
            print(f" ------------------ ROUND {compteur+1} -----------------")
            current_round= []
            playerslists_ordering = sorted(playerslists, key=lambda x: x["score"], reverse=True)
            print(playerslists_ordering)
            for i in range (0, 8):
                p1 = playerslists_ordering[i]["nom"]   
                for j in range (i+1, 8):
                    p2 = playerslists_ordering[j]["nom"]
                    print(p1, p2)
                    match = ((playerslists_ordering[i]["nom"], playerslists_ordering[j]["nom"]), (playerslists_ordering[i]["score"], playerslists_ordering[j]["score"]))
                    #print("*"*20)
                    #print(match)
                    if self.check_match(p1, p2, matchs) == False:       
                        if self.check_player(p1, p2, current_round) == False:
                            current_round.append(match)
                            matchs.append(match)
                            self.update_score(playerslists_ordering[i], playerslists_ordering[j])
                            #print("match créé", match)
                            break
                        else:
                            pass
                            #print("match non-ajouté", match)
                    else:
                        pass
                        #print("match non créé", match)

            print(matchs)
            compteur += 1
            if len(current_round) == 0:
                next = False
                print("plus de matchs possibles")

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

    def update_score(self, p1, p2):
        p1.points = random.randint(0, 20)
        p2.points = random.randint(0, 20)
        if p1.points > p2.points:
            p1["score"] += 1
        elif p2.points > p1.points:
            p2["score"] += 1
        else:
            p1["score"] += 0.5
            p2["score"] += 0.5