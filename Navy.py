from OnePieceCharacters import Characters


class Marine(Characters):
    def __init__(self, name, age, devil_fruit, voice_actor, rank):
        super().__init__(name, age, devil_fruit, voice_actor)
        self.rank = rank

    def show_rank(self):
        return f"{self.name} has a Naval ranking of {self.rank}."
