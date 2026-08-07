class Student:
    def __init__(self, name, surname, age, avg_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_score = avg_score
    def change_avg_score(self):
        print(f'Ви змінюєте середній бал для студента {self.name} {self.surname}, введіть новий середній бал: ')
        while True:
            try:
                new_avg_score = float(input())
                self.avg_score = new_avg_score
                break
            except ValueError:
                print("Помилка! Необхідно ввести число.")

student1 = Student("Іван", "Студентський", 16, 85.7)
print(f'Студент {student1.age} років {student1.name} {student1.surname},  його середній бал: {student1.avg_score}')
student1.change_avg_score()
print(f'Середній бал студента {student1.age} років {student1.name} {student1.surname} складає {student1.avg_score}')

