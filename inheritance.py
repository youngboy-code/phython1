
#parent class/super class?
class animal:
    def sound(self):
        print("animal is speaking")

#Child class/subclass/derived class
class Duck(animal):
    def move(self):
        print("duck is swimming")


class caterpillar(Duck):
    def slide(self):
        print("caterpillar is slithering")

a = animal()
a.sound()
d = Duck()
d.sound()

c = caterpillar()
c.move()