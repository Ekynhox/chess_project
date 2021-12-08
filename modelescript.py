import random


class Player:
    def __init__(self, score, id):
        self.id = id
        self.score = score

    def __str__(self):
        return f"p{self.id}: {self.score:.1f}"

    def __repr__(self):
        return str(self)


class Tournament:
    def __init__(self, players):
        self.players = players
        self.turns = []
        self.history = []

    @property
    def last_turn(self):
        return self.turns[-1]

    def set_matchs(self):
        choices = [(0.0, 1.0), (1.0, 0.0), (0.5, 0.5)]
        for p1, p2 in self.last_turn:
            s1, s2 = random.choice(choices)
            p1.score += s1
            p2.score += s2

    def get_possible_turns(self):
        turns = []
        matchs_history = []
        for _ in range(7):
            turn = []
            players = self.players[:]
            while players:
                p1 = players.pop(0)
                match = []
                found = None
                for index, p2 in enumerate(players):
                    match = (p1, p2)
                    if match not in matchs_history:
                        found = index
                        break
                if found is not None:
                    players.pop(found)
                    matchs_history.append(match)
                    turn.append(match)
            turns.append(turn)
        return [turn for turn in turns if turn not in self.history]

    def create_turn(self):
        turn = []
        best_turn = []
        possible_turns = self.get_possible_turns()
        lowest_difference = 1000

        for turn in possible_turns:
            difference = max([abs(p1.score - p2.score) for (p1, p2) in turn])
            if difference < lowest_difference:
                lowest_difference = difference
                best_turn = turn

        self.history.append(best_turn)
        self.turns.append(best_turn)


    players = [Player(0, index) for index in range(1, 9)]
tournament = Tournament(players)

for _ in range(4):
    tournament.create_turn()
    tournament.set_matchs()
    print("last turn:", tournament.last_turn)