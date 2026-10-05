#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n: int):
    i = 0

    while i <= n:
        if i % 2 == 0:
            yield i
            i = i + 1
        else:
            i = i + 1

rtyme = even_numbers(12)

while True:
    try:
        print(next(rtyme))
    except StopIteration:
        break

#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N
print('__________')
def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        a, b = b, a + b

tryfunction = fibonacci(10)
while True:
    try:
        print(next(tryfunction))
    except StopIteration:
        break


