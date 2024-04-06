from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print("Боец атакует голыми руками.")
class Monster:
    def __init__(self, name):
        self.name = name

    def encounter(self, fighter):
        print(f"{fighter.name} выбирает {type(fighter.weapon).__name__}.")
        fighter.attack()
        print(f"{self.name} побежден!")

# Создаем бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч и сражается с монстром
fighter.changeWeapon(Sword())
monster.encounter(fighter)

# Боец выбирает лук и сражается с монстром
fighter.changeWeapon(Bow())
monster.encounter(fighter)
