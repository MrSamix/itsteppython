#task 1
user = input("Введи рядок: ")
user1 = user.lower()
user2 = user.replace(" ", "")
if user2[0::] == user2[::-1]:
    print("Цей рядок є паліндромом")
else:
    print("Цей рядок не є паліндромом")

#task 2

user = input("Введи рядок: ")
slovo = input("Введи зарезервоване слово: ")
splited = user.split()

userreplaced = user.replace(slovo,slovo.upper())
print(userreplaced)

#task 3
user = input("Введи текст: ")
newtext = user.split(". ")
print(f"К-сть речень в цьому тексті = {len(newtext)}")