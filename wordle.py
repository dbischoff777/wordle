import random
from rich import print

class Wordle:
    def __init__(self):
        self.word = []
        with open("wordle.txt", "r") as db:
            self.word = random.choice([line.rstrip('\n') for line in db])
            self.num_guesses = 0
            self.guess_dict = {
                0: [" "]*5,
                1: [" "]*5,
                2: [" "]*5,
                3: [" "]*5,
                4: [" "]*5,
                5: [" "]*5,
            }

    def draw_board(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("================")

    def get_user_input(self):
        user_guess = input("Enter a five letter word: ")
        while len(user_guess) != 5:
            user_guess = input("not valid, enter a five letter word: ")

        user_guess = user_guess.lower()
        for idx, char in enumerate(user_guess):	
            if char in self.word:
                if char == self.word[idx]:
                    char = f"[green]{char}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dict[self.num_guesses][idx] = char
        
        self.num_guesses += 1
        return user_guess
                


    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_input()

            if user_guess == self.word:
                self.draw_board()
                print(f"You won! The word was {self.word}")
                break

            if self.num_guesses > 5:
               self.draw_board()
               print(f"You lost! The word was {self.word}")         
               break

if __name__ == "__main__":
    game = Wordle()
    game.play()