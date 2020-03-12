class Critter(object):
    def __init__(self):
        print("Появилась на свет новая зверюшка!")
    def talk(self):
        print("Привет. Я - зверюшка - экземпляр класса Critter.")

crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nНажмите Ent, чтобы выйти")
