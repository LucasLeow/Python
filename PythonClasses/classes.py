class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def get_fullName(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee("Lucas", "Leow", 10000)
print(emp_1.get_fullName())