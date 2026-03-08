from random import choice

class Model:
    def __init__(self):
        self.guesses = []
        self.guess = ""
        self.attempts = 0
        self.choose_word = [
            "apple", "river", "mountain", "computer", "language", "keyboard", "window", "garden", "ocean", "forest",
            "cloud", "energy", "music", "picture", "library", "science", "future", "freedom", "success", "dream",
            "challenge", "growth", "wisdom", "courage", "peace", "travel", "adventure", "friendship", "family", "knowledge",
            "design", "strategy", "system", "network", "signal", "planet", "galaxy", "nature", "balance", "vision"
        ]
        self.word = ""
        self.left_attempts = 0
        self.score = 0
        self.difficulty = ""
        self.choose_difficulty = {
        # Difficulty, Points, Attempts, Max word length
            "Easy" : [25, 12, 5],
            "Medium" : [40, 8, 7],
            "Hard" : [60, 5, 10]
        }
        
    def guess_a_word(self, text):
        if text is None:
            return "enter a letter"
        text = text.strip().lower()
        if not text:
            return "enter a letter"
        if len(text) != 1:
            return "enter a single letter"
        if not text.isalpha():
            return "only letters allowed"
        if text in self.guesses:
            return "you already guessed that letter"
        self.guess = text
        self.guesses.append(text)
        return

    def create_a_word(self):
        max_word_length = self.choose_difficulty[self.difficulty][2]
        filtered_words = []
        for word in self.choose_word:
            if len(word) <= max_word_length:
                filtered_words.append(word)
        if not filtered_words:
            filtered_words = self.choose_word[:]
        self.word = choice(filtered_words)
        
    def set_max_attempts(self, text):
        for difficult in self.choose_difficulty:
            if difficult == text:
                self.left_attempts = self.choose_difficulty[difficult][1]
                
    def check_guess(self, text):
        if text is None:
            return "enter a letter"
        text = text.strip().lower()
        if not text:
            return "enter a letter"
        if not text.isalpha():
            return "only letters allowed"
        if len(text) != 1:
            return "enter a single letter"

        if text in self.word:
            unique_letters = set(self.word)
            if unique_letters.issubset(set(self.guesses)):
                return "Congrats you guessed the word right!"
            return self.left_attempts, "Correct!"
        else:
            self.left_attempts -= 1
            return self.left_attempts, "Wrong guess!"

    def set_difficulty(self, text):
        if text in self.choose_difficulty.keys():
            self.difficulty = text
            return self.difficulty
            
    def score_after_right_guess(self):
        if self.difficulty in self.choose_difficulty:
            self.score += self.choose_difficulty[self.difficulty][0]
            return self.score
    
    def reset(self):
        pass

class View:
    def __init__(self):
        pass
    
    def show_word(self, word, guesses):
        result = ""
        for letter in word:
            if letter in guesses:
                result += letter 
            else:
                result += "_"
            result += " "
        print("The word:", result)
        
    def show_message(self, message):
        print(message)

    def show_score(self, score):
        print(f"Current score: {score}")

    def ask_for_guess(self):
        return input("Guess a letter: ")

    def show_attempts(self, attempts):
        print(f"Still {attempts} attempts left.")

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_game(self):
        while True:
            diff = input("Choose difficulty (Easy / Medium / Hard): ")
            if self.model.set_difficulty(diff):
                self.model.set_max_attempts(diff)
                break
            else:
                self.view.show_message("Invalid difficulty. Try again.")

        self.model.create_a_word()
        self.model.guesses = []
        self.model.score = 0 

        while self.model.left_attempts > 0:
            self.view.show_word(self.model.word, self.model.guesses)
            self.view.show_attempts(self.model.left_attempts)
            guess = self.view.ask_for_guess()
            result = self.model.guess_a_word(guess)
            if result:
                self.view.show_message(result)
                continue

            check = self.model.check_guess(guess)
            if isinstance(check, str):
                self.view.show_message(check)
                if "Congrats" in check:
                    self.model.score_after_right_guess()
                    self.view.show_score(self.model.score)
                    break
            else:
                left, msg = check
                self.view.show_message(msg)
                self.view.show_attempts(left)
        
        if self.model.left_attempts == 0:
            self.view.show_message(f"Game over! The word was '{self.model.word}'.")

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start_game()