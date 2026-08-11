'''Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
(враховуються як великі так і маленькі).
 Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''

word = input('Input a word with \'h\' or \'H\': ')
while True:
    if 'h' in word or 'H' in word:
        break
    else:
        word = input('Input a word with \'h\' or \'H\': ')