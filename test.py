import random


class Player:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.points = Player.random()
        self.score = score

    def __str__(self):
        return f"{self.name} - {self.score}"
    def random():
        return random.randint(0, 20)

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

for player in playerslists_ordering:
    print(player)    

def check_match(p1, p2, matchs):
    for item in matchs:
        if (p1 == item[0][0] and p2 == item[0][1]) or (p1 == item[0][1] and p2 == item[0][0]):
            return True
    return False


match_round2 = []

def check_player(p1, p2, match_round2):    
    for item in match_round2: 
        if (p1 == item[0][0] or p1 == item[0][1]) or (p2 == item[0][0] or p2 == item[0][1]):  
            return True           
    return False

for i in range (0, 8):
    for j in range (i+1, 8):
        p1 = playerslists_ordering[i].name
        p2 = playerslists_ordering[j].name
        match = ((playerslists_ordering[i].name, playerslists_ordering[j].name), (playerslists_ordering[i].score, playerslists_ordering[j].score))
        print(match)
        if check_match(p1, p2, matchs) == False:       
            if check_player(p1, p2, match_round2) == False:
                match_round2.append(match)
                matchs.append(match)
                print(matchs)
                break
            else:
                print("match non-ajouté", match)
        else:
            print("pas de match", match)
        

print("*"*20)
for match in matchs:
    print(match)
    pass

#écrire une deuxième condition pour vérifier si le joueur en cours n'a pas déjà effectué 

# - # ------------------ ROUND 3 -----------------

#méthode récursive -> se renseigner
