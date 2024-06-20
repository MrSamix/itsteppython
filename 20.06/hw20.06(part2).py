user = input("Введи арифметичний вираз(23+12), підтримуються дії(+,-,*,/): ")
if "+" in user:
    formatednum = user.split('+')
    print(f"Результат = {float(formatednum[0]) + float(formatednum[1])}")
elif "-" in user:
    formatednum = user.split('-')
    print(f"Результат = {float(formatednum[0]) - float(formatednum[1])}")
elif "*" in user:
    formatednum = user.split('*')
    print(f"Результат = {float(formatednum[0]) * float(formatednum[1])}")
elif "/" in user:
    formatednum = user.split('/')
    print(f"Результат = {float(formatednum[0]) / float(formatednum[1])}")