import random

#task 1

tupleown = (1,[22,33,11,22,66,44])
print(tupleown)
tupleown[1][0] = 11
print(tupleown)

#task 2
tuplepow = (random.randint(-100,100) for i in range(10))
tuplenew = []
for i in tuplepow:
    if i % 2 == 0:
        tuplenew.append(i)
else:
    print(tuple(tuplenew))


#task 3
tupleown = (11,22,33,44,55)
elem1 = tupleown[0:1]
elem4 = tupleown[-2:-1]

print([tupleown[2]])


#task 4
tupleown = (random.randint(0,1000) for i in range(random.randint(1,200)))
tuplesort = sorted(tupleown)
print(tuplesort)

#task 5
list1 = [1,2]
list2 = [2]
set1 = set(list1)
set2 = set(list2)
setunion = set1.union(set2)
setintersection = set1.intersection(set2)
setdifference = set1.difference(set2)
setsimetricdifference = set1.symmetric_difference(set2)

print(setunion)
print(setintersection)
print(setdifference)
print(setsimetricdifference)

#task 6
tuple1 = (1,2,32,4,52,6,7,8,9,10)
tuple2 = (1,2,3,4,5,6,7,8,9,10)
set1 = set(tuple1)
set2 = set(tuple2)
set3 = set1.intersection(set2)
tuplenew = tuple(set3)

print(set1)
print(set2)
print(set3)
print(tuplenew)

#task 7
list_of_numbers = [22,55,22,555,966,11,120,511254,25165,11,154,11,3333,21,2,0,1111,222,33,36,32,5,4,12,2,51,1,2,212]
list_of_unic_numbers = set(list_of_numbers)
sort_list_of_numbers = sorted(list_of_unic_numbers)
tuplenumbers = tuple(sort_list_of_numbers)
print(tuplenumbers)

#task 8
list_of_lists = [[1],[2],[3]]
list_of_lists[0] = set(list_of_lists[0])
list_of_lists[1] = set(list_of_lists[1])
list_of_lists[2] = set(list_of_lists[2])
print(list_of_lists)
list_of_lists[0] = list_of_lists[0].union(list_of_lists[1])
list_of_lists[0] = list_of_lists[0].union(list_of_lists[2])
print(list_of_lists)

#task 9
lists = []
templist = []
for i in range(10):
    templist = []
    for i in range(3):
        templist.append(random.randint(1,100))
    templist = tuple(templist)
    lists.append(templist)
print(lists)

set_from_list = set(lists)
print(set_from_list)

#task 10
tuple_of_numbers = (22,33,44,55,66,77,88,99,100)
dobutok = 1
suma = sum(tuple_of_numbers)
print(f"sum = {suma}")
print(f"avg = {suma/len(tuple_of_numbers)}")
for i in tuple_of_numbers:
    dobutok *= i
print(f"dobutok = {dobutok}")


#task 11
tuple1 = ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4))
for i in range(4):
    for elem in range(4):
        print(tuple1[i][elem])


#task 12
my_list = [1,2,2,3,3,3,4,4,4,4,4]

my_set = set(my_list)
print(my_set)

from collections import Counter
counter = Counter(my_list)
most_common = counter.most_common(1)
print(f"Елементи, що зустрічаються найчастіше: {most_common}")

#task 13
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tuple_of_sets = tuple(set(sublist) for sublist in list_of_lists)
print(tuple_of_sets)