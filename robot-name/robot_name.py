import random
import string

class Robot(object):
    def __init__(self):
        # define letters and numbers
        self.letters = string.ascii_uppercase
        self.numbers = string.digits
        # define leng (letters and numbers)
        self.lengLetters = 2
        self.lengNumbers = 3
        # generate random
        self.serialName = ''.join(random.sample(self.letters, self.lengLetters))
        self.serialNumber = ''.join(random.sample(self.numbers, self.lengNumbers))
        # concatenates
        self.name = self.serialName + self.serialNumber

    def reset(self):
        self.letters = string.ascii_uppercase
        self.numbers = string.digits
        self.lengLetters = 2
        self.lengNumbers = 3
        # with seed, random restart
        random.seed("some random")
        self.serialName = ''.join(random.sample(self.letters, self.lengLetters))
        self.serialNumber = ''.join(random.sample(self.numbers, self.lengNumbers))
        self.name = self.serialName + self.serialNumber
