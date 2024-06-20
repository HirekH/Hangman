import os
import random

class Hangman:
    
    easy_hang = {"easyone", "easytwo", "easythree"}
    medium_hang = {"mediumone", "mediumtwo", "mediumthree"}
    difficult_hang = {"difficlutone", 'difficulttwo", "difficultthree'}

    def __init__(self, difficulty):
        self.hang_string = self.select_hang_string(difficulty)
        self.init_graph()

    def select_hang_string(self, difficulty):
        if difficulty <= 1:
            return self.easy_hang[randomint(0,len(self.easy_hang))]
        if difficulty == 2:
            return self.medium_hang[randomint(0,len(self.medium_hang))]
        if difficulty > 2:
            return self.difficult_hang[randomint(0,len(self.difficult_hang))]
        
