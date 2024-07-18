import math

#task 1
number = int(input("введи додатнє число: "))
try:
  if number < 0:
    raise ValueError
except ValueError:
  print("Введено від'ємне число")
else:
  print(f"Факторіал числа {number} = {math.factorial(number)}")



#task 2
def task2_1(number):
  return f"Факторіал числа {number} = {math.factorial(number)}"

number = int(input("введи додатнє число: "))
try:
  if number < 0:
    raise ValueError
except ValueError:
  print("Введено від'ємне число")
else:
  print(task2_1(number))


def task2_2(number):
  try:
    if number < 0:
      raise ValueError
  except ValueError:
    return "Введено від'ємне число"
  else:
    return f"Факторіал числа {number} = {math.factorial(number)}"


number = int(input("введи додатнє число: "))
print(task2_2(number))


#task 3
list_of_numbers = []
for i in range(5):
  number = int(input("Введи число: "))
  list_of_numbers.append(number)


while True:
  print("1.Відображення списку.\n2.Отримання максимального значення у списку.\n3.Отримання мінімального значення у списку.\n4.Відображення значення елемента за індексом, введеним користувачем.\n5.Видалення елемента за індексом, введеним користувачем.\n6. Вихід з програми.")
  choose = int(input("Виберіть дію: "))
  if choose == 1:
    print(list_of_numbers)
  elif choose == 2:
    print(max(list_of_numbers))
  elif choose == 3:
    print(min(list_of_numbers))
  elif choose == 4:
    index = int(input("Введіть індекс: "))
    try:
      result = list_of_numbers[index]
    except:
      print("Ви ввели індекс, який не існує")
    else:
      print(result)
  elif choose == 5:
    index = int(input("Введіть індекс: "))
    try:
      list_of_numbers.pop(index)
    except:
      print("Ви ввели індекс, який не існує")
    else:
      print(list_of_numbers)
  elif choose == 6:
    print("Вихід...")
    break



#task 4
def task4_1(result):
  return result

list_of_numbers = []
for i in range(5):
  number = int(input("Введи число: "))
  list_of_numbers.append(number)

print("1.Відображення списку.\n2.Отримання максимального значення у списку.\n3.Отримання мінімального значення у списку.\n4.Відображення значення елемента за індексом, введеним користувачем.\n5.Видалення елемента за індексом, введеним користувачем.\n6. Вихід з програми.")
choose = int(input("Виберіть дію: "))
if choose == 1:
  print(task4_1(list_of_numbers))
elif choose == 2:
  result = max(list_of_numbers)
  print(task4_1(result))
elif choose == 3:
  result = min(list_of_numbers)
  print(task4_1(result))
elif choose == 4:
  index = int(input("Введіть індекс: "))
  try:
    result = list_of_numbers[index]
  except:
    print("Ви ввели індекс, який не існує")
  else:
    print(task4_1(result))
elif choose == 5:
  index = int(input("Введіть індекс: "))
  try:
    list_of_numbers.pop(index)
  except:
    print("Ви ввели індекс, який не існує")
  else:
    print(task4_1(list_of_numbers))
elif choose == 6:
  print("Вихід...")

def task4_2(list_of_numbers):
    print("1.Відображення списку.\n2.Отримання максимального значення у списку.\n3.Отримання мінімального значення у списку.\n4.Відображення значення елемента за індексом, введеним користувачем.\n5.Видалення елемента за індексом, введеним користувачем.\n6. Вихід з програми.")
    choose = int(input("Виберіть дію: "))
    if choose == 1:
      return list_of_numbers
    elif choose == 2:
     return max(list_of_numbers)
    elif choose == 3:
      return min(list_of_numbers)
    elif choose == 4:
      index = int(input("Введіть індекс: "))
      try:
        result = list_of_numbers[index]
      except:
        return "Ви ввели індекс, який не існує"
      else:
        return result
    elif choose == 5:
      index = int(input("Введіть індекс: "))
      try:
        list_of_numbers.pop(index)
      except:
        return "Ви ввели індекс, який не існує"
      else:
        return list_of_numbers
    elif choose == 6:
      return "Вихід..."


list_of_numbers = []
for i in range(5):
  number = int(input("Введи число: "))
  list_of_numbers.append(number)
print(task4_2(list_of_numbers))