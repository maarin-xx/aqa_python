#Напишіть декоратор, який логує аргументи та результати викликаної функції.
import logging

logging.basicConfig(level=logging.INFO)

def logging_func(func):
    def wrapper(*args, **kwargs):
        logging.info('func called')
        logging.info(f'args = {args}, kwargs = {kwargs}')
        result =  func(*args, **kwargs)
        logging.info(f' result = {result}')
        return result
    return wrapper

@logging_func
def sum_numbers(num1, num2):
    return num1 + num2

test = sum_numbers(1,2)

#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def execute_function(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(f'Exception raised: {e}')
    return wrapper

@execute_function
def divide_number(num1, num2):
    return num1 / num2

test2 = divide_number(1,'abc')