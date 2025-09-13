# ********************* Simple Game Example Explaining use of (self, other) ********************* 

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # This method needs a target to act upon
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        Damage = int(input("Enter Damage: " ))

        target.health -= Damage
        print(f"{target.name}'s health is now {target.health}.")

hero = Player("Aragorn", 100)
orc = Player("Grishnákh", 50)

# We are calling the method on the 'hero' object.
# So, 'self' is hero, and the argument 'target' is orc.
hero.attack(orc)
hero.attack(orc)