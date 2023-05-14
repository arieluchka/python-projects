import random
# random string generator for passwords etc


class RandomPasswordGenerator:
    def __init__(self, num_characters, num_special, num_numbers):
        self._letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self._special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '_', '-', '+', '=']
        self._number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self._password = None
        self._requirements = {
            "characters" : num_characters,
            "special_characters" : num_special,
            "numbers" : num_numbers
        }

    def __str__(self):
        print(f"your pass is {self._password}")

    def rand_letter(self):
        return self._letters[random.randrange(0, len(self._letters))]

    def rand_special(self):
        return self._special_characters[random.randrange(0, len(self._special_characters))]

    def rand_number(self):
        return self._number_list[random.randrange(0, len(self._number_list))]

    def add_to_pass(self, character):
        self._password += character

    def build_pass(self):
        # was possible to do with "for" loop but decreasing the num_characters value will help with tracking whats left
        while self._requirements["characters"] > 0:
            test = random.randrange(0, 2)
            if test == 0:
                self.add_to_pass(self.rand_letter())
            elif test == 1:
                self.add_to_pass(self.rand_special())
            else:
                self.add_to_pass(self.rand_number())
            self._requirements["characters"] -= 1
        print(self._password)


if __name__ == '__main__':
    password = RandomPasswordGenerator(10, 2, 2)
    RandomPasswordGenerator.build_pass