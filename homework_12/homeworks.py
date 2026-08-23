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

#task2

'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
 які присутні в lst1. Данні в лісті можуть бути будь якими'''

def new_list_with_str_only(lst):

    lst2 = [k for k in lst if type(k) is str]
    return lst2

#task 3

'''
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
'''
data1 = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "22.11", "None, 1", "1, True"]


def sum_list(data):
    res = []
    for i in (data):
        digits = i.split(",")
        try:
            digits_float = [float(i) for i in digits]
            res.append(sum(digits_float))

        except ValueError:
            res.append("Cannot do this")

    return res

print(sum_list(data1))