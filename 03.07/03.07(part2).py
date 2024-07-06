def task1(list_of_numbers):
    result = 1
    for num in list_of_numbers:
        result *= num
    return result

list_of_numbers = [2,2.5,3,3.5,4,4.5,5,5.5]
print(task1(list_of_numbers))

def task2(list_of_numbers):
    return min(list_of_numbers)

print(task2(list_of_numbers))

def task3(list_of_numbers):
    count = 0
    for num in list_of_numbers:
        if num < 2:
            continue
        is_prime = True
        a = 2
        while a < num:
            if num % a == 0:
                is_prime = False
                break
            a += 1
        if is_prime:
            count += 1
    return count

list_of_numbers1 = [2,3,4,5,6,7,8,9,10,12,15,20,24,28]
print(task3(list_of_numbers1))

def task4(list_of_numbers, target):
    count = list_of_numbers.count(target)
    while target in list_of_numbers:
        list_of_numbers.remove(target)
    print(f"Змінений список: {list_of_numbers}")
    return f"К-сть {target} = {count}"

list_of_numbers2 = [2,2,2,2,2,2,3,4,5,6,7,8,9,10]
print(task4(list_of_numbers2, 2))


def task5(list1, list2):
    return list1 + list2

list1 = [1,2,3]
list2 = [4,5,6]

print(task5(list1, list2))

def task6(list_of_numbers, power):
    return [num**power for num in list_of_numbers]

list_of_numbers1 = [2,3,4,5,6,7,8,9,10]
print(task6(list_of_numbers1, 2))