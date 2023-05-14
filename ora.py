class Car:

    def __init__(self, color, mark, carrying=0):
        self.color = color
        self.mark = mark

        if carrying != 0:
            self.carrying = carrying

    def sound(self):
        print("Машина", self.mark, "Посигналила бип")

    def long_sound(self):
        print("Машина", self.mark, "Посигналила бип-бип")


first = Car("Синий", "Субару", 100)
second = Car("Белый", "Камаз", 500)
print(second.carrying)
first.sound()
second.long_sound()