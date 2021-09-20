

class Player:

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def __gt__(self, other):
        if self.choice == "rock" and other.choice == "scissors":
            return True
        elif self.choice == "paper" and other.choice == "rock":
            return True
        elif self.choice == "scissors" and other.choice == "paper":
            return True
        return False

    
