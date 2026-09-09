class Plumber():
    """
    Creates a plumber
    """
    character_type = 'plumber' # <- Atención con esto
    def __init__(self, name):
        self.name = name
    def jump(self):
        print(self.name, "jumps!")
    def movement(self, direction):
        print(self.name, "moves", direction)


class Villain():
    """
    Creates a villain
    """
    character_type = 'villain'
    def __init__(self, name):
        self.name = name
    def jump(self):
        print(self.name, "jumps!")
    def movement(self, direction):
        print(self.name, "moves", direction)


class Character():
    """
    Creates a game character
    """
    def __init__(self, name):
        self.name = name
    def jump(self):
        print(self.name, "jumps!")
    def movement(self, direction):
        print(self.name, "moves", direction)


class CarnivorousPlant(Character):
    """
    Creates a princess
    """
    
    character_type = 'carnivorous plant'
    def jump(self): # <- Sobrescribimos esta función...
        print("I can't jump you moron!")
    def movement(self, direction): # <- ... y también esta
        print("Is this some kind of joke?")