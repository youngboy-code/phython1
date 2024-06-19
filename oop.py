
class Person:

    def __init__(self, firstname,courses,gender):
        self.firstname = firstname
        self.course = courses
        self.gender = gender

    def study(self):

       print(self.firstname, "is studying")

student1 = Person("sam","cybersecuriry","male")
student1.study()

student2 = Person("Neema","data science","female")
student2.study()

student3 = Person("sam","cybersecuriry","male")
student3.study()