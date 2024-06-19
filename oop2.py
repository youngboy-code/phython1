
class car:

    def __init__(self,model,color,manufacturer,yop,):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yop


    def speed(self):
        print("The manufacturer of",self.model,"is",self.manufacturer)

car1 = car("M12","white","BMW","2012")
car1.speed()
car2 = car("GTR","Black","Nissan","2013")
car2.speed()
car3 = car("g-class","White","Mercedes","2012")
car3.speed()