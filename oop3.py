
class device:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom

    def crush(self):
        print(self.model,"has crushed")

computer = device("HP",2008)
computer.crush()
laptop = device("Dell",1992)