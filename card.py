class Card():
    def __init__(self, suit, number):
        self._suit = suit
        self._value = number
        self._number = number

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    @property
    def number(self):
        return self._number

    @suit.setter
    def suit(self, suit):
        suits = ["hearts",
                 "clubs",
                 "diamonds",
                 "spades"]

        if suit in suits:
            self._suit = suit
        else:
            print("That's not a suit!")

    @number.setter
    def number(self, number):
        numbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        face = {"A": 1, "J": 10, "Q": 10, "K": 10}

        if number in numbers:
            if face[number]:
                self._number = number
                self._value = int(face[number])
                print(face[number])
            else:
                self._number = number
                self._value  = int(number)
                print(face[number])
        else:
            print("That's not a valid number")

    def __repr__(self):
        # return self.number + " of " + self.suit
        return f"{str(self.number)} of {str(self.suit)}"

my_card = Card("Hearts", 7)
another_card = Card("Dinosaurs", 2)

print(my_card.value)

# https://projects.raspberrypi.org/en/projects/deck-of-cards/5