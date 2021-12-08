import random

class Player:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.points = Player.random()
        self.score = score
    def random():
        return random.randint(0, 20)

dice = Player.random()


name = input("Entrée le nom du joueur:")
player1 = Player(name='Pierre', age=22, score = 0)
player2 = Player(name='Lucie', age=25, score = 0)
player3 = Player(name='Victor', age=19, score = 0)
player4 = Player(name="Damien", age=12, score = 0)




if player1.points > player2.points:        
    print(player1.name + ' gagne le match 1')
    player1.score += 1
elif player2.points > player1.points:
    print(player2.name + ' gagne le match 1')
    player2.score += 1
else:
    print(player1.name + ' et '+player2.name + ' font egalite sur le match 1')
    player1.score += 0.5
    player2.score += 0.5


if player3.points > player4.points:        
    print(player3.name + ' gagne le match 1')
    player3.score += 1
elif player4.points > player3.points:
    print(player4.name + ' gagne le match 1')
    player2.score += 1
else:
    print(player3.name + ' et '+player4.name + ' font egalite sur le match 1')
    player3.score += 0.5
    player4.score += 0.5

if player1.points > player3.points:        
    print(player1.name + ' gagne le match 2')
    player1.score += 1
elif player3.points > player1.points:
    print(player3.name + ' gagne le match 2')
    player3.score += 1
else:
    print(player1.name + ' et '+player3.name + 'font egalite sur le match 2')
    player1.score += 0.5
    player3.score += 0.5


if player2.points > player4.points:        
    print(player2.name + 'gagne le match 2')
    player2.score += 1
elif player4.points > player2.points:
    print(player4.name +  'gagne le match 2')
    player4.score += 1
else:
    print(player2.name + ' et '+player4.name + 'font egalite sur le match 3')
    player2.score += 0.5
    player4.score += 0.5

if player1.points > player4.points:        
    print(player1.name + 'gagne le match 3')
    player1.score += 1
elif player4.points > player1.points:
    print(player4.name + ' gagne le match 3')
    player4.score += 1
else:
    print(player1.name + ' et '+player4.name + 'font egalite sur le match 3')
    player1.score += 0.5
    player4.score += 0.5

if player2.points > player3.points:        
    print(player2.name + ' gagne le match 3')
    player2.score += 1
elif player3.points > player2.points:
    print(player3.name + ' gagne le match 3')
    player3.score += 1
else:
    print(player2.name + ' et '+player3.name + 'font egalite sur le match 3')
    player2.score += 0.5
    player3.score += 0.5


print(player1.name, player1.score, player2.name , player2.score, player3.name, player3.score, player4.name, player4.score)

if player1.score > player2.score and player1.score > player3.score and player1.score > player4.score: 
    print(player1.name + " gagne le match.")

elif player2.score > player1.score and player2.score > player3.score and player2.score > player4.score: 
    print(player2.name + " gagne le matche.")

elif player3.score > player1.score and player3.score > player2.score and player3.score > player4.score: 
    print(player3.name + " gagne le match.")

else :
    print(player4.name + " gagne le match")


# mettre en place les écrans (MVC : V) : nom, age, score input de l'utilisateur
# se renseigner sur tinyDB