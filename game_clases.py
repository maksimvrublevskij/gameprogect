class Warrior:
    def __init__(self, healht=100, stamina=100):
        self.health = healht
        self.stamina = stamina
    def introduces(self):
        print('----------------------')
        print(f'Class: {self.__class__.__name__}',
        f'\nHealth: {self.health}',
        f'\nStamina: {self.stamina}')
        print('-----------------------')
    def heals(self, target):
        print('-------------------')
        print(f'{self.__class__.__name__} накладывает повязку из целебных трав на {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц выносливости')
        print('-------------------')
    def attacks(self, target):
        print('-------------------')
        print(f'{self.__class__.__name__} наносит удар мечом по {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target.health}')
        print('-------------------')
class Mage:
    def __init__(self, health=60, mana=100):
        self.health = health
        self.mana = mana
    def introduces(self):
        print('----------------------')
        print(f'Class: {self.__class__.__name__}',
        f'\nHealth: {self.health}',
        f'\nMana: {self.mana}')
        print('-----------------------')
    def heals(self, target):
        print('-------------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.mana} единиц магии')
        print('-------------------')
    def attacks(self, target):
        print("----------------")
        print(f'{self.__class__.__name__} наносит удар мечом по {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target.health}')
        print("----------------")


unit1 = Warrior(100, 50)
unit2 = Warrior(70, 120)
unit3 = Mage()
unit4 = Mage(50, 110)


unit1.introduces()
unit4.introduces()

unit4.heals(unit1)


unit1.introduces()
unit4.introduces()

print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
