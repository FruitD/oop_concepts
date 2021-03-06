from OnePieceCharacters import Characters


class Pirate(Characters):
    def __init__(self, name, age, devil_fruit, voice_actor, crew, bounty):
        super().__init__(name, age, devil_fruit, voice_actor)
        self.bounty = bounty
        self.crew = crew

    def show_bounty(self):
        return f"{self.name} has a bounty of {self.bounty}."

    def show_crew(self):
        return f"{self.name} is a part of the {self.crew}!"
