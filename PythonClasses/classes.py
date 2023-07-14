class Employee:

    num_employees = 0
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_employees += 1  # Want to modify for all instances

    def get_fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # if self used, only instance raise_amount is modified
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount) # if Employee used, all instance raise_amount modified

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod  # Alternative Constructor to parse string input
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        # Monday = 0
        # Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.get_fullName(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


class Developer(Employee):
    raise_amt = 1.1  # Developer class raise_amt does not affect parent class raise_amt

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) Also valid but not typically used
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.get_fullName())


dev_1 = Developer("Lucas", "Leow", 60000, "Python")
dev_2 = Developer("Tom", "Tim", 40000, "Java")
mgr_1 = Manager("Sue", "Ann", 80000, [dev_1])
mgr_1.add_employee(dev_2)

print(mgr_1.email)
mgr_1.print_emps()

print(dev_1.__repr__())
print(dev_1.__str__())


emp_1 = Employee("lucas", "leow", 50000)
emp_2 = Employee("Timmy", "Tan", 30000)

print(emp_1 + emp_2)
print(len(emp_1))
