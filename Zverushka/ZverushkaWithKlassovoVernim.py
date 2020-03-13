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



crit1 = Critter("Барсик")
crit2 = Critter("Шарик")

print("Вывод объекта crit1 на экран: ")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name: ")
print(crit1.name)
print("\n")

print("Вывод объекта crit2 на экран: ")
print(crit2)
print("Непосредственный доступ к атрибуту crit2.name: ")
print(crit2.name)

input("\n\nНажмите Ent, чтобы выйти")
