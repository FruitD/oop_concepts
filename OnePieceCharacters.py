class Characters:
    def __init__(self, name, age, devil_fruit, bounty):
        self.name = name
        self.age = age
        self.devil_fruit = devil_fruit
        self.bounty = bounty

    def isGood(self):
        return False

    def show_bounty(self):
        return {"{} has a bounty of {}.".format(self.name, self.bounty)}

    def show_fruit(self):
        if self.devil_fruit is not None:
            return {"{}'s devil fruit power is {}".format(self.name, self.devil_fruit)}
        else:
            return {'{} does not have a devil fruit power.'}

    def show_age(self):
        return {"{} is {} years old!".format(self.name, self.age)}
