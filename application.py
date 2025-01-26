from Python.students import Students


class Application(Students):

    def __init__(self, name, age, std, gender):
        super().__init__(name, age, std)
        self.gender = gender

student4 = Application('Shivamani', 24, 'MTech', 'Male')
student4.print_details()
print(student4.gender)
