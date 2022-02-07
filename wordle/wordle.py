from datetime import date
from game import Game

possible_words = ["train", "moist", "lamps", "clock", "prick", "roast"] # TODO: move to "word_list.txt" and load it 


def get_word_guess():
    while True:
        word = input("Guess: ").lower()
        if len(word) != 5:
            print("Not a 5 letter word. \r")
        elif word not in possible_words:
            print("Not in word list. \r")
        else:
            return word


def main():

    # current date
    today = date.today()

    # clean game for today
    game = Game(today)

    while not game.is_finished():
        word = get_word_guess()
        game.current_guess(word)


if __name__ == '__main__':
    main()
