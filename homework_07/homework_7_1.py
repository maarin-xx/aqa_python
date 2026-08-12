import re
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            print('Табличка множення до добутку 25 сформована ')
            break

        if result < 25:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))

        if multiplier == 9:
            break

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
print('_'*50)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two(first, second):
    return first + second


a = 5
b = 6
print(f'Сумма чисел {a} та {b} довірнює: {sum_two(a, b)}')
print('_'*50)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
list_of_digits = list(range(10, 55))

def avg_list_of_digits(list_of_digits):
    return sum(list_of_digits) / len(list_of_digits)


print(f'List of numbers: {list_of_digits} ')
print(f'The arithmetic mean of a list of numbers: {avg_list_of_digits(list_of_digits)}')
print('_'*50)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
input_string = input('Provide your string: ')

def reverse_string(input_string):
    return input_string[::-1]


print(f'Reverse the string: {reverse_string(input_string)}')
print('_'*50)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
words = input('Provide your words: ').split()

def longest_word(words):
    return max(words, key=len)


print(f'Longest word: {longest_word(words)}')
print('_'*50)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
print('_'*50)


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

def if_count_symbol_more_than_10(my_string):
    """
    Returns True if the string contains more than 10 unique characters,
    otherwise returns False.

    :param my_string: string to check
    :return: True or False
    """

    unique_symbols = set(my_string)
    return len(unique_symbols) > 10

my_string = input("Input your string: ")
print(f'If your string has more than 10 unique symbols: {if_count_symbol_more_than_10(my_string)}')
print('_'*50)


# task 8
'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
 які присутні в lst1. Данні в лісті можуть бути будь якими'''

def new_list_with_str_only(lst):
    """
    Creates a new list containing only strings from the input list.

    :param lst1: input list
    :return: list containing only string elements
    """
    lst2 = [k for k in lst1 if type(k) is str]
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', (1, 2, 3), {'name': 'Josie', }]
print(new_list_with_str_only(lst1))
print('_'*50)

# task 9
#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def sum_even_numbers(lst):
    """
    Returns the sum of even numbers from input list.
    If the list contains non-numeric elements, returns a message and sum = 0.

    :param lst: input list containing numbers and other elements
    :return: message and sum of even numbers, or message and 0 if a non-numeric element is found
    """
    sum = 0
    for i in lst:
        if type(i) == int:
            if i % 2 == 0:
                sum = sum + i
        else:
            sum = 0
            message = 'В листі зустрічаються символи, які не є числами, сума = '
            return message, sum

    message = 'Сума парних чисел обчислена'
    return message, sum

list1 = [1, 2, 3, 4, 5, 9, 11, 12, 45, 54, 22]
list2 = [1, 2, 3, 4, 5, 9, 11, '2', 12, 45, 54, 22]
print(sum_even_numbers(list2))
print(sum_even_numbers(list1))
print('_'*50)


# task 10
""" Перевірте чи починається якесь речення з "By the time" (заданої строки).
"""
def check_the_beginning_of_sentence(text, start_string):
    """
    Returns sentences that start with the given string.

    :param text: input text
    :param start_string: string to check at the beginning of sentences
    :return: list of sentences starting with the given string
    """
    result = []
    text_by_sentence = re.split(r'[.!?]+\s*' ,text)[:-1]
    for sentence in text_by_sentence:
        if sentence.startswith(start_string):
            result.append(sentence)

    return result


print(check_the_beginning_of_sentence('Once upon a time. Upon. Once!', 'Once'))
