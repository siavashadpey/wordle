from termcolor import colored


class Game():
    def __init__(self, date):
        self._today = date
        self._guess_nb = 0
        self._total_guesses = 5
        self._word = "roast"  # TODO: choose today-th element in the "words_to_guess.txt"
        self._is_finished = False
        self._is_won = False

    def is_finished(self):
        return self._is_finished

    def current_guess(self, word):
        word = word.lower()
        self._guess_nb += 1
        self._is_won = word.lower() == self._word
        self._is_finished = self._is_won or (self._guess_nb == self._total_guesses)
        self._update(word)

    def _update(self, word):

        string = ""
        for i, letter in enumerate(word):
            if self._correct_letter_and_location(i, letter):
                color = 'green'
            elif self._correct_letter_only(letter):
                color = 'yellow'
            else:
                color = 'red'
            string += colored(letter, color)

        print("{:d}/{:d}: {:s}".format(self._guess_nb, self._total_guesses, string))

        if self._is_won:
            print("")
            print("You won!")
        elif self._is_finished:
            print("")
            print("Game over!")

    def _correct_letter_and_location(self, i, letter):
        return self._word[i] == letter

    def _correct_letter_only(self, letter):
        return letter in self._word
