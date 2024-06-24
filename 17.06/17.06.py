#task 1
num1 = int(input("Введи 1 число: "))
num2 = int(input("Введи 2 число: "))
parnisum = 0
parnicount = 0
neparnisum = 0
neparnicount = 0
kratni9sum = 0
kratni9count = 0
for i in range(num1, num2 + 1):
  if i % 2 == 0:
    parnisum += i
    parnicount += 1
  elif i % 9 == 0:
    kratni9sum += i
    kratni9count += 1
  elif i % 2 != 0:
    neparnisum += i
    neparnicount += 1
else:
  print(f"Сума парних чисел = {parnisum}")
  print(f"Сума непарних чисел = {neparnisum}")
  print(f"Сума чисел кратних 9 = {kratni9sum}")
  print(f"Середнє арифметичне парних чисел = {parnisum/parnicount}")
  print(f"Середнє арифметичне непарних чисел = {neparnisum/neparnicount}")
  if kratni9count == 0:
    print("Середнє арифметичне чисел кратних 9 = 0")
  else:
    print(f"Середнє арифметичне чисел кратних 9 = {kratni9sum/kratni9count}")

#task 2
symbol = input("Введи символ для заповнення: ")
repeat = int(input("Введи кількість рядків: "))
for i in range(repeat):
  print(symbol)

#task 3
while True:
  num = int(input("Enter a number: "))
  if num == 7:
    print("Good bye!")
    break
  elif num > 0:
    print("Number is positive")
    continue
  elif num < 0:
    print("Number is negative")
    continue
  else:
    print("Number is equal to zero")
    continue

#task 4
sum = 0
maxnum = 0
minnum = 0
while True:
  num = int(input("Enter a number: "))
  sum += num
  if num == 7:
    print("Good bye!")
    break
  elif num > maxnum:
    maxnum = num
  if minnum == 0 or num < minnum:
    minnum = num
  print(f"Сума чисел = {sum}")
  print(f"Максимальне число = {maxnum}")
  print(f"Мінімальне число = {minnum}")