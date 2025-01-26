# A class is an object constructor a blueprint for creating the objects

class Students:

    def __init__(self, name, age, standard):
        # constructor method
        self.name = name
        self.age = age
        self.standard = standard

    def print_details(self):
        print("My name is "+ self.name)
        print("Studing in "+ self.standard)

student1 = Students('Apurva', 16, 'Inter')
student2 = Students('Shiva', 24, 'Graduate')

student1.print_details()
student2.print_details()
