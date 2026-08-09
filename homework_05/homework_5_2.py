# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

#task1
# 1 - Add your new record o the beginning of the given list

people_records.insert(0, ('Wilma', 'Zurh', 53, 'Seamstress', 'Minnesota'))
print(people_records)

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)


# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
list_to_check = [people_records[6], people_records[10], people_records[13]]
result = True
for person in list_to_check:
    if not person[2] >= 30:
        result = False
print(f'If all people in modified list have age >=30: {result}')