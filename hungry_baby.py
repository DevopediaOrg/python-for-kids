import threading
import queue
import random
import time
import pygame


class PiggyBank:
    def __init__(self, value=0):
        self.__coins = value

    def add_coins(self, value):
        self.__coins += value

    def get_balance(self):
        return self.__coins


class Baby(threading.Thread):
    favourites = (
        'pizza', 'pancake', 'idli', 'icecream', 
        'sandwich', 'burger', 'noodles', 'pineapple'
    )

    def __init__(self, plate, piggy):
        threading.Thread.__init__(self)
        self.__plate = plate
        self.num_items = 0
        self.__piggy = piggy
        self.to_eat = None
        pygame.mixer.init()
        pygame.mixer.music.load("assets/baby-crying.mp3")

    def run(self):
        while self.__piggy.get_balance() > 0:
            # Baby selects one of its favourite food
            self.to_eat = random.choice(self.favourites)

            # How long will the baby wait: 3 seconds or less
            waittime = min(3, 100 / self.__piggy.get_balance())

            item = print(get_prompt(self.__piggy.get_balance(), self.to_eat), end="")

            try:
                # Baby sees food on plate
                item = self.__plate.get(block=True, timeout=waittime)
                if item == self.to_eat:
                    # Baby's current favourite food
                    self.dontcry()
                    self.__piggy.add_coins(2 * len(self.to_eat))
                    self.num_items += 1
                else:
                    # Baby cries and deducts 5 coins
                    print("Baby: I want to eat only {}".format(self.to_eat))
                    self.cry()
                    self.__piggy.add_coins(-5)

            except queue.Empty:
                # Nothing on the plate: baby is angry and deducts 10 coins
                self.cry()
                self.__piggy.add_coins(-10)

        print("\nBaby: I ate {} items. Thank you!!!".format(self.num_items))
        
    def cry(self):
        pygame.mixer.music.play()

    def dontcry(self):
        pygame.mixer.music.stop()


def get_prompt(coins, want):
    return "\r{}\rCoins {:04d}; Baby wants {:10s}: ".format(' '*40, coins, want)


if __name__ == '__main__':
    # Initialize
    piggy = PiggyBank(20)
    plate = queue.Queue()

    # Allow the baby to ask for food
    baby = Baby(plate, piggy)
    baby.start()

    # Run as long as there are enough coins
    while piggy.get_balance() > 0:
        item = input(get_prompt(piggy.get_balance(), baby.to_eat))
        plate.put(item)
        time.sleep(0.1)