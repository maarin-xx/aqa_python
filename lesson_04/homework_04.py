import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Task 1")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(" .... ", " ")
print("Task 2")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
print("Task 3")
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
a = re.findall('h', adwentures_of_tom_sawer)
print("Task 4")
print(f'Літера "h" зустрічається {len(a)} раз(ів)')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
cap_letter = re.findall(r'\b[A-Z]', adwentures_of_tom_sawer)
print("Task 5")
print(f'З Великої літери починається {len(cap_letter)} слів в тексті')
#['T', 'A', 'B', 'M', 'T', 'B', 'B', 'T', 'B', 'F', 'J', 'M', 'A', 'T']

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_pos = adwentures_of_tom_sawer.find("Tom")
second_pos = adwentures_of_tom_sawer.find("Tom", first_pos+1)
print("Task 6")
print(f'слово Tom зустрічається вдруге на {second_pos} позиції')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]+\s*',adwentures_of_tom_sawer)[:-1]
print("Task 7")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 8")
print(adwentures_of_tom_sawer_sentences[3].lower())
print(adwentures_of_tom_sawer_sentences)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 9")
c = 0
for i in range(0, len(adwentures_of_tom_sawer_sentences)):
    if adwentures_of_tom_sawer_sentences[i].startswith("By the time"):
        print(f'Речення, починається з "By the time": {adwentures_of_tom_sawer_sentences[i]}')
        c = c + 1
if c == 0:
        print('В тесксті нема жодного речення, що починається з "By the time" ')


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sent = adwentures_of_tom_sawer_sentences[len(adwentures_of_tom_sawer_sentences)-1]
count_of_words = len(last_sent.split())
print("Task 10")
print(f'Кількість слів останнього речення: {count_of_words}')
