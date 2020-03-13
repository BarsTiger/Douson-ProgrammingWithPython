class Critter(object):
    total = 0

    @staticmethod

    def status():
        print("\nВсего зверюшек сейчас", Critter.total)

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1


print("Нахожу значение атрибута клсса Critter.total:", end= " ")
print(Critter.total)
print("\nСоздаю зверюшек.")


crit1 = Critter("Звеюшка 1")
crit2 = Critter("Звеюшка 2")
crit3 = Critter("Звеюшка 3")
crit4 = Critter("Звеюшка 4")

Critter.status()

print("\nОбращаюсь к атрибуту класса через объект:", end= " ")
print(crit1.total)

input("\n\nНажмите Ent, чтобы выйти")
