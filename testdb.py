from tinydb import TinyDB, Query
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
    def saveplayer(self):
        pass


db = TinyDB('db.json')
p1 = Player(name='name', age='age', score=0)
p2 = Player(name='name', age='age', score=0)

print("insérez le nom du joueur 1")
player1_name = input()
print("insérez le nom du joueur 2")
player2_name = input()
print("insérez l'âge du joueur 1")
player1_age = input()
print("insérez l'âge du joueur 2")
player2_age = input()

db.insert_multiple([
        {p1.name : player1_name, p1.age : player1_age},
        {p2.name: player2_name, p2.age: player2_age}])

for item in db:
    print(item)

 