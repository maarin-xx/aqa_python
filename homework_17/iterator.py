#Реалізуйте ітератор для зворотного виведення елементів списку.

def iterable_rev(list):
    my_iterable_rev = iter(list[::-1])
    while True:
        try:
            print(next(my_iterable_rev))
        except StopIteration:
            break

iterable_rev([1,2,3,4,5,13,17])
print('____________')

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class OddIterator:
    def __init__(self, n):
        self.current = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1
        raise StopIteration


tryodd = OddIterator(12)
for number in tryodd:
    print(number)