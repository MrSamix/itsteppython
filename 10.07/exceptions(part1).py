#task 1
name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))
try:
  if age < 0 or age > 130:
      raise ValueError
except ValueError:
  print("Некоректний вік")
else:
  print(f"Привіт, {name}! Твій вік — {age}")


#task2
def task2_1(name, age):
  return f"Привіт, {name}! Твій вік — {age}"

name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))
try:
  if age < 0 or age > 130:
      raise ValueError
except ValueError:
  print("Некоректний вік")
else:
  print(task2_1(name, age))



def task2_2(name, age):
  try:
    if age < 0 or age > 130:
        raise ValueError
  except ValueError:
    return "Некоректний вік"
  else:
    return f"Привіт, {name}! Твій вік — {age}"


name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))
print(task2_2(name, age))


#task3
list_of_numbers = []
for _ in range(5):
  number = int(input("Введи додатнє число: "))
  list_of_numbers.append(number)

try:
  for number in list_of_numbers:
    if number < 0:
      raise ValueError
except ValueError:
  print("В списку є від'ємні числа")
else:
  print(f"Сума чисел = {sum(list_of_numbers)}")


#task4
def task4_1(list_of_numbers):
  return f"Сума чисел = {sum(list_of_numbers)}"


list_of_numbers = []
for _ in range(5):
  number = int(input("Введи додатнє число: "))
  list_of_numbers.append(number)

try:
  for number in list_of_numbers:
    if number < 0:
      raise ValueError
except ValueError:
  print("В списку є від'ємні числа")
else:
  print(task4_1(list_of_numbers))

def task4_2():
  list_of_numbers = []
  for _ in range(5):
    number = int(input("Введи додатнє число: "))
    list_of_numbers.append(number)

  try:
    for number in list_of_numbers:
      if number < 0:
        raise ValueError
  except ValueError:
    return "В списку є від'ємні числа"
  else:
    return f"Сума чисел = {sum(list_of_numbers)}"



print(task4_2())