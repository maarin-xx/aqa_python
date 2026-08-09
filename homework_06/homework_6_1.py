#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

my_string = input("Input your string: ")
unic = set(my_string)
# if len(unic) > 10:
#     print(True)
# else:
#     print(False)

result = False
result = len(unic) > 10
print(result)