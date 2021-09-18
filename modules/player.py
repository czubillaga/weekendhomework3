class Player:

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def __gt__(self, other):
        if self.choice == "Rock" and other.choice == "Scissors":
            return True
        elif self.choice == "Paper" and other.choice == "Rock":
            return True
        elif self.choice == "Scissors" and other.choice == "Paper":
            return True
        return False