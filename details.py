from Python.students import Students, student1


class Details(Students):

     def __init__(self, name, age, std, address):
         Students.__init__(self, name, age, std)
         self.address = address


student3 = Details('Apurva Jain', 24, 'Btech')
student3.print_details()
print(student3.address)
