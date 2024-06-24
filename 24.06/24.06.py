#task 1
import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = list1 + list2
print(list3)

#task 2

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = []
for elem in list1 + list2:
    if elem not in list3:
        list3.append(elem)
print(list3)

#task 3

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = []
for elem in list1:
    if elem in list2 and elem not in list3:
        list3.append(elem)
print(list3)

#task 4

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = []
for elem in list1:
    if elem not in list2 and elem not in list3:
        list3.append(elem)
for elem in list2:
    if elem not in list1 and elem not in list3:
        list3.append(elem)
print(list3)

#task 5

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = [min(list1), max(list1), min(list2), max(list2)]
print(list3)