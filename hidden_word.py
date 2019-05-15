import string
import random
import sys
import re
import os
import itertools
import colorama


class HiddenWordPuzzle:
    def __init__(self, word, size):
        if len(word) > size:
            print("Error: Word is longer than grid size. Quitting...")
            exit(1)
        
        self.make_grid(size)
        self.insert_word(word)

    def make_grid(self, size):
        self.__grid = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(random.choice(string.ascii_lowercase))
            self.__grid.append(row)
        self.__numrows = self.__numcols = size

    def print_grid(self, reveal_word=False):
        for rownum, row in enumerate(self.__grid, start=1):
            print("{:2d} | ".format(rownum), end="")
            for cell in row:
                if reveal_word and cell.isupper():
                    print("\033[92m{}\033[0m ".format(cell), end='')
                else:
                    print("{} ".format(cell.upper()), end='')
            print("")

        print("{}\n   | ".format('-'*(4+2*len(self.__grid[0]))), end='')

        for colnum, _ in enumerate(self.__grid[0]):
            print("{} ".format(string.ascii_lowercase[colnum]), end='')
        print("")

    def insert_word(self, word):
        self.__word = word.upper()
        self.__direction = random.choice(('right', 'down', 'diagonal'))

        start_left, start_right = 0, len(self.__grid) - len(word)
        self.__start_rowpos = rowpos = random.randint(start_left, start_right)
        self.__start_colpos = colpos = random.randint(start_left, start_right)

        for char in self.__word:
            self.__grid[rowpos][colpos] = char
            if self.__direction == 'right':
                colpos += 1
            elif self.__direction == 'down':
                rowpos += 1
            else:
                colpos += 1
                rowpos += 1

    def validate_answer(self, ans):
        matches = re.findall(r'([a-z])(\d+)-([a-z])(\d+)', ans)
        if not matches:
            print("Not a valid input. Try again.")
            return False

        start_col, start_row, end_col, end_row = matches[0]
        start_col = string.ascii_lowercase.find(start_col)
        start_row = int(start_row) - 1
        end_col = string.ascii_lowercase.find(end_col)
        end_row = int(end_row) - 1

        # Check start and end points
        if start_row > end_row or start_col > end_col:
            print("Start positions can't be greater than end positions. Try again.")
            return False

        # Check dimensions
        if start_col >= self.__numcols or end_col >= self.__numcols or \
           start_row >= self.__numrows or end_row >= self.__numrows:
            print("Your input exceeds board dimensions. Try again.")
            return False

        # Check the length and direction
        word_len_h = end_col - start_col + 1
        word_len_v = end_row - start_row + 1
        if word_len_h == len(self.__word) and word_len_v == 1 and self.__direction == 'right' or \
           word_len_v == len(self.__word) and word_len_h == 1 and self.__direction == 'down' or \
           word_len_v == len(self.__word) and word_len_h == len(self.__word) and self.__direction == 'diagonal':
           pass
        else:
            print("Either word length or direction is wrong. Try again.")
            return False

        row_indices = itertools.repeat(start_row, word_len_h) if word_len_v == 1 else range(start_row, end_row+1)
        col_indices = itertools.repeat(start_col, word_len_v) if word_len_h == 1 else range(start_col, end_col+1)
        guess_word = "".join(self.__grid[i][j] for i, j in zip(row_indices, col_indices))
        if guess_word != self.__word:
            print("Wrong answer. Try again.")
            return False

        return True


def clear_console():
    if sys.platform.startswith('win'):
        os.system("cls")
    else:
        os.system("clear")


def read_answer():
    return input("\nEnter your answer (example, d2-d8): ")


if __name__ == "__main__":
    colorama.init()
    puzzle = HiddenWordPuzzle('hello', 10) # sys.argv[1], int(sys.argv[2])
    clear_console()
    puzzle.print_grid()
    if puzzle.validate_answer(read_answer()):
        puzzle.print_grid(True)
        print("CONGRATS! Your answer is correct!")
