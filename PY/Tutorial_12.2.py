# TITLE: CLASSES AND OBJECTS
# TITLE: EXERCISE_01
# 1. Create a simple game character class with health, attack and heal methods.
class Character:
    def __innit__(self, name, health=100, strength=15):
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength

    def attack(self, attack):
        target.health -= damage
        print(f"{self.name} attacked {target.name} for {damage} damage!")

    def heal(self,amount):
        self.heal += amount
        print(f"{self.name} healed for {amount}. Current health: {self.health}")


# hero = Character("Knight")
# enemy = Character("Goblin", 50)

print(f"Character: {hero.name}")
print(f"Current health: {hero.health}")