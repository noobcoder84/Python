
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'

    def full_name(self):
        return "Your name is: {} {}".format(self.first, self.last)
        

emp1 = Employee(input("first name: "), input("last name: "))
print(Employee.full_name(emp1))
print("Your email address will be: " + emp1.email)
