class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        self.annual_salary += 5000
        return f"{self.first_name} {self.last_name} your annual salary is {self.annual_salary}"

    def custom_raise(self):
        self.annual_salary += int(input('custom raise'))
