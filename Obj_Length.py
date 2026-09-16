class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)

team = Team(["A", "B", "C", "D"])

print(len(team))