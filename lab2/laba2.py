from abc import ABC, abstractmethod

class GameObject:
    def __init__(self, id, name, x, y):
        if id <= 0:
            raise ValueError("ID должен быть положительным")
        self.__id = id
        self.name = name
        self.x = x
        self.y = y
    def getId(self):
        return self.__id
    def getName(self):
        return self.name
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        if hp < 0:
            raise ValueError("Здоровье не может быть отрицательным")
        self.__hp = hp

    def isAlive(self):
        return self.__hp > 0

    def getHp(self):
        return self.__hp

    def receiveDamage(self, damage):
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self.__hp = max(0, self.__hp - damage)

class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self.built = built
    def isBuilt(self):
        return self.built

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

class Archer(Unit, Attacker, Moveable):
    def __init__(self, id, name, x, y, hp, damage):
        super().__init__(id, name, x, y, hp)
        self.damage = damage
    def attack(self, unit):
        unit.receiveDamage(self.damage)
    def move(self, x, y):
        self.x = x
        self.y = y

class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, built, damage):
        super().__init__(id, name, x, y, built)
        self.damage = damage
    def attack(self, unit):
        unit.receiveDamage(self.damage)

class MobileHouse(Building, Moveable):
    def move(self, x, y):
        self.x = x
        self.y = y

archer = Archer(1, "Лучник", 0, 0, 100, 25)
enemy = Archer(2, "Враг", 5, 5, 60, 10)
fort = Fort(3, "Крепость", 10, 10, True, 40)
house = MobileHouse(4, "Дом", 2, 2, True)
archer.attack(enemy)
fort.attack(enemy)
print(enemy.getHp(), enemy.isAlive())
archer.move(7, 7)
house.move(7, 7)
print(archer.getX(), archer.getY())
print(house.getX(), house.getY())