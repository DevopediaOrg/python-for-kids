import string
import random
import colorama
import sys


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

    def print_grid(self):
        for row in self.__grid:
            for cell in row:
                if cell.isupper():
                    print("\033[92m{}\033[0m ".format(cell), end='')
                else:
                    print("{} ".format(cell.upper()), end='')
            print("") # to force a newline

    def insert_word(self, word):
        self.__direction = random.choice(('right', 'down', 'diagonal'))

        start_left, start_right = 0, len(self.__grid) - len(word)
        self.__start_rowpos = rowpos = random.randint(start_left, start_right)
        self.__start_colpos = colpos = random.randint(start_left, start_right)

        for char in word.upper():
            self.__grid[rowpos][colpos] = char
            if self.__direction == 'right':
                rowpos += 1
                colpos += 1
            elif self.__direction == 'down':
                colpos += 1
            else:
                rowpos += 1

if __name__ == "__main__":
    colorama.init()
    puzzle = HiddenWordPuzzle(sys.argv[1], int(sys.argv[2]))
    puzzle.print_grid()