class Hero:
    def __init__(self, name, super_hero_name, age, height):
        self.name = name
        self.super_hero_name = super_hero_name
        self.age = age
        self.height = height
        print("я был рождён и моё геройское имя", super_hero_name)

    def hit(self, enemy_name):
        print(self.super_hero_name, "Ударил кулаком", enemy_name)


my_hero = Hero("Куджо Джотаро", "Джо джо", 19, 193)
enemy = Hero("Дио Брандо", "ДИО",  100, 193)

print("Возраст персонажа", my_hero.age, my_hero.super_hero_name, my_hero.name)
my_hero.hit(enemy.super_hero_name)
enemy.hit(my_hero.super_hero_name)

print("Yare yare yare daze ,ora ora ora ora ora ora ora ora")
print("Za Warudo, muda muda muda muda muda muda muda muda muda muda muda muda")
print("Эпичная музыка")