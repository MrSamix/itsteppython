#task 1
num1 = int(input("Введи початок діапазону: "))
num2 = int(input("Введи кінець діапазону: "))

for i in range(num1, num2+1):
    if i % 7 == 0:
        print(i)

#task 2
num1 = int(input("Введи початок діапазону: "))
num2 = int(input("Введи кінець діапазону: "))
count = 0
for i in range(num1, num2+1):
    print(i)
#порядок спадання
for i in range(num2, num1-1, -1):
    print(i)

#числа кратні 7
for i in range(num1, num2+1):
    if i % 7 == 0:
        print(i)
    if i % 5 == 0:
        count += 1
else:
    print(f"К-сть чисел кратних 5 = {count}")

#task 3
num1 = int(input("Введи початок діапазону: "))
num2 = int(input("Введи кінець діапазону: "))

for i in range(num1, num2+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)