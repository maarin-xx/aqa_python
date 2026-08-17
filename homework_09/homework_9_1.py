"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:
Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""
class Rhombus:

    def __init__(self, side_a, angle_a):

        self.side_a = side_a
        self.angle_a = angle_a
        #self.angle_b = 180 - angle_a


    def __setattr__(self, name, value):

        if name == 'side_a':

            if not isinstance(value, (float, int)):
                raise TypeError('The side of a rhombus can be expressed only by numbers')

            if value <= 0:
                raise ValueError('The side of a rhombus must be greater than 0')


        if name in ('angle_a', 'angle_b'):

            if not isinstance(value, (float, int)):
                raise TypeError('The angle of a rhombus can be expressed only by numbers')

            if value <= 0 or value >= 180:
                raise ValueError('The angle of a rhombus must be between 0 and 180')

            # angle_n = 'angle_b' if name == 'angle_a' else 'angle_a' #можемо не знати який кут задано, а який змінюємо
            # if angle_n in self.__dict__:
            #     if value + self.__dict__[angle_n] != 180:
            #         raise ValueError('The sum of two adjacent angles of a rhombus must be 180')

            self.__dict__[name] = value

            if name == 'angle_a':
                self.__dict__['angle_b'] = 180 - value
            else:
                self.__dict__['angle_a']= 180 - value
            return


        self.__dict__[name] = value

    def __str__(self):
        return f'Rhombus with: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}'



r7 = Rhombus(1, 170 ) # angle_a=170, angle_b=10
print(r7)
r7.angle_a=1 # angle_a=1, angle_b=179
print(r7)
r7.angle_b=15 # angle_a=165, angle_b=15
print(r7)