#task1
"""
Завдання 1
Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
 які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
  а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
 Цей клас представляє керівника з команди розробників.
  Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
  а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department, **kwargs):
        self.department = department
        super().__init__(name, salary, **kwargs)


class Developer(Employee):
    def __init__(self, name, salary, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(name, salary, **kwargs)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(name, salary, department, **kwargs)

    def check_attr(self):
        attr = ['name', 'salary', 'department', 'programming_language']
        #attr = [hasattr(self, attr) for attr in attr if hasattr(self, attr)]
        result = all(hasattr(self, attr) for attr in attr)
        return f'If there are all attr: {result}'