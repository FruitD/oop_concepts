class Characters:
    def __init__(self, name, age, devil_fruit, voice_actor):
        self.name = name
        self.age = age
        self.devil_fruit = devil_fruit
        self.voice_actor = voice_actor

    def show_fruit(self):
        if self.devil_fruit is not None:
            return f"{self.name}'s devil fruit power is the {self.devil_fruit} fruit."
        else:
            return f'{self.name} does not have a devil fruit power.'

    def show_age(self):
        return f"{self.name} is {self.age} years old!"

    def show_va(self):
        return f"{self.name} is voiced by {self.voice_actor}."
