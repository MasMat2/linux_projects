

class Employee:

    num_of_emps = 0
    raise_amount = 5
    first = "adsd"
    last = "qrwee"

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self): # Never forget the self argument for methods
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount



emp_1 = Employee("Corey", "Shafer", 50000)
emp_2 = Employee("Test", "sub", 10)
emp_2.apply_raise()

emp_2.pay_check = "la"
print(Employee.__dict__)
print("---------------------------------")
print(emp_1.num_of_emps)
del Employee.num_of_emps
print("---------------------------------")
print(emp_2.num_of_emps)
del emp_2.pay_check
print("---------------------------------")
print(emp_2.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#
# emp_1.raise_amount = 1.05
#
# print(emp_1.__dict__)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# emp_1.fullname()
# print(Employee.fullname(emp_1))
#
#
# print(emp_1.fullname())
# print(emp_2.fullname())
#
# emp_1.first = "Corey"
# emp_1.last = "Shafer"
# emp_1.email = "-------------@company.com"
# emp_1.pay = 50000
#
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "-------------------@company.com"
# emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)
