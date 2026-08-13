"""
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі
та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись
через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль
площу та периметр кожної.
"""
from abc import abstractmethod, ABC


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def return_result(self):
        s = self.area()
        p = self.perimeter()
        return f's = {s} and p = {p}'


class Square(Figure):

    def __init__(self, side):
        self.__side = side

    def area(self):
        s = self.__side * self.__side
        return s

    def perimeter(self):
        p = 4 * self.__side
        return p

class Rectangle(Figure):

    def __init__(self, sidea, sideb):
        self.__sidea = sidea
        self.__sideb = sideb

    def area(self):
        s = self.__sidea * self.__sideb
        return s

    def perimeter(self):
        p = 2 * (self.__sidea+ self.__sideb)
        return p

class Rhombus(Figure):

    def __init__(self, side, h):
        self.__side = side
        self.__h = h

    def area(self):
        s = self.__side * self.__h
        return s

    def perimeter(self):
        p = 4 * self.__side
        return p

square1 = Square(4)
rhombus1 = Rhombus(1, 2)
rectangle1 = Rectangle(8, 10)
figures = [square1, rhombus1, rectangle1]

for f in figures:
    print(f.return_result())