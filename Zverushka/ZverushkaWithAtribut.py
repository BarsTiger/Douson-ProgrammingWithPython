class Critter(object):
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):
        print("Привет. Я - зверюшка - экземпляр класса Critter.")

crit1 = Critter("Барсик")
crit1.talk()
crit2 = Critter("Шарик")
crit2.talk()

print("Вывод объекта crit1 на экран: ")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name: ")
print(crit1.name)


input("\n\nНажмите Ent, чтобы выйти")