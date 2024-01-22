class Player():
    def __init__(self,name,difficulty):
        self.name = name
        self.difficulty = difficulty
    def getguess(self):
        guess = input("Enter a character or word as a guess: ")
        try:
            if (guess == ""):
                raise ValueError
        except ValueError:
            print ("Invalid input. Please guess a character or word.")
        return guess