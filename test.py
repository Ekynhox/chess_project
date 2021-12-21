import random
from modeles import Player



dice = Player.random()

round = 4

nombre_de_joueurs = 8

p1 = Player(name="p1", age=10, score=0)
p2 = Player(name="p2", age=10, score=0)
p3 = Player(name="p3", age=10, score=0)
p4 = Player(name="p4", age=10, score=0)
p5 = Player(name="p5", age=10, score=0)
p6 = Player(name="p6", age=10, score=0)
p7 = Player(name="p7", age=10, score=0)
p8 = Player(name="p8", age=10, score=0)

groupe1 = [p1, p2, p3, p4]
groupe2 = [p5, p6, p7, p8]


# - # ------------------ ROUND 1 -----------------
matchs = []

for i in range(round):
    if groupe1[i].points > groupe2[i].points:
        groupe1[i].score += 1
        print(groupe1[i].name + " gagne")
    elif groupe2[i].points > groupe1[i].points:
        groupe2[i].score += 1
        print(groupe2[i].name + " gagne")
    else:
        groupe1[i].score += 0.5
        groupe2[i].score += 0.5
    
    match = ((groupe1[i].name, groupe2[i].name), (groupe1[i].score, groupe2[i].score))
    matchs.append(match)
    
for match in matchs:
    print(match)
 
# - # ------------------ ROUND 2 -----------------
playerslists = groupe1 + groupe2
playerslists_ordering = sorted(playerslists, key=lambda x: x.score, reverse=True)

#for player in playerslists_ordering:
 #   print(player)    

def check_match(p1, p2, matchs):
    for item in matchs:
        if (p1 == item[0][0] and p2 == item[0][1]) or (p1 == item[0][1] and p2 == item[0][0]):
            return True
    return False

def check_player(p1, p2, match_round2):    
    for item in match_round2: 
        if (p1 == item[0][0] or p1 == item[0][1]) or (p2 == item[0][0] or p2 == item[0][1]):  
            return True           
    return False

def update_score(p1, p2):
    if p1.points > p2.points:
        p1.score += 1
    elif p2.points > p1.points:
        p2.score += 1
    else:
        p1.score += 0.5
        p2.score += 0.5


next = True

compteur = 1
while compteur < 9: 

#for k in range(1, 4):
    print(f" ------------------ ROUND {compteur} -----------------")
    current_round= []
    playerslists_ordering = sorted(playerslists, key=lambda x: x.score, reverse=True)
    print(playerslists_ordering)
    for i in range (0, 8):
        p1 = playerslists_ordering[i].name
        #print(p1)
        for j in range (i+1, 8):
            p2 = playerslists_ordering[j].name
            print(p1, p2)
            match = ((playerslists_ordering[i].name, playerslists_ordering[j].name), (playerslists_ordering[i].score, playerslists_ordering[j].score))
            #print("*"*20)
            #print(match)
            if check_match(p1, p2, matchs) == False:       
                if check_player(p1, p2, current_round) == False:
                    current_round.append(match)
                    matchs.append(match)
                    update_score(playerslists_ordering[i], playerslists_ordering[j])
                    #print("match créé", match)
                    break
                else:
                    pass
                   # print("match non-ajouté", match)
            else:
                pass
                #print("match non créé", match)

    print(current_round)
    compteur += 1
    if len(current_round) == 0:
        next = False
        print("plus de matchs possibles")
  
# vérifier le bug de match, et mettre le code sous fonction "generate_round", et implémenter le tinydb