from OnePieceCharacters import Characters


class Pirate(Characters):
    def __init__(self, crew, name, age, devil_fruit, bounty):
        super().__init__(name, age, devil_fruit, bounty)
        self.crew = []

