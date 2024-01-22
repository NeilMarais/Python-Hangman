import math
import time
import random
from player import Player

class Hangman():
    def __init__(self,currentplayer):
        self.charsFound = []
        self.difficulty = currentplayer.difficulty
        self.wordlist = self.generateWordList()
        self.chosenWord = self.chooseWord()
        self.lettersGuessed = [] 
        self.turns = 0
        self.winner = False
        self.loser = False
        
    
    def generateWordList(self):
        wordlist = []
        mode = self.difficulty
        if mode == "n":
            file = open("Standard Words.txt","r")
            wordlist = [line.rstrip() for line in file]
        else:
            file = open("Hard Words.txt","r")
            wordlist = [line.rstrip() for line in file]
        return wordlist

    def chooseWord(self):
        word = self.wordlist[random.randrange(0,len(self.wordlist))]
        for i in range (len(word)):
            self.charsFound.append("-")
        return word
    
    def checkWord(self,guess):
        if(guess == self.chosenWord):
            print("")
            print("Correct!")
            self.winner = True
        else:
            print("")
            print("Wrong!")
    
    def checkChar(self, guess):
        self.lettersGuessed.append(guess)
        i =0
        found = False
        for letter in self.chosenWord:
            if (letter == guess):
                self.charsFound[i] = letter
                found = True
            i += 1
        if(found):
            print("")
            print("Correct!")
            print("")
            self.checkWin()
        else:
            print("")
            print("Wrong!")
            print("")
        
    
    def checkWin(self):
        foundword = ""
        for letter in self.charsFound:
            foundword = foundword + letter
        if(foundword == self.chosenWord):
            self.winner = True
    
    def printInfo(self,currentplayer):
         print("")
         print("You have " + str(10 - self.turns) + " guesses left.")
         print("You have already guessed the following characters: " + str(self.lettersGuessed))
         print("The word is " +str(len(self.chosenWord)) + " letters long.")
         print("You currently know the following letters: " + str(self.charsFound))
    def incTurns(self):
        self.turns += 1    
    def setLoser(self, bool):
        self.loser = bool
    def getDifficulty(self):
        return self.difficulty

    
def play(game,currentplayer):

    while (game.winner == False and game.loser== False):
        game.printInfo(currentplayer)
        guess = str(currentplayer.getguess())
        game.incTurns()    
        if (len(guess) == 1):
            game.checkChar(guess)
        else:
            game.checkWord(guess)
        
        if (game.turns == 10 and game.loser== False):
            game.setLoser(True)
        time.sleep(.8)
    
    if (game.winner ==True):
        print(currentplayer.name + " wins! The correct word was " + game.chosenWord + ". It was guessed in " + str(game.turns) + " guesses.")
    else:
        print("Computer wins! The correct word was: " + game.chosenWord+ ".")



                
                

if __name__ == "__main__":
    print("")
    print("Welcome to Hangman. You will have 10 guesses to find the word the computer has randomly selected. Follow the instructions below to get started.")
    print("")
    name = input("Please enter your name:")
    while (name == ""):
        print("Your name cannot be empty.")
        name = input("Please enter your name:")

    difficulty = input("Select the difficulty you'd like to play (n for normal and h for hard):")
    while (difficulty!= "n" and difficulty != "h"):
        print("You must enter n or h for the difficulty.")
        difficulty = input("Select the difficulty you'd like to play (n for normal and h for hard):")
    currentplayer = Player(name,difficulty)
    Ongoing = Hangman(currentplayer)
    play(Ongoing, currentplayer)

       
            