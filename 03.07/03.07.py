from colorama import Fore
#task 1
def task1():
  print(Fore.LIGHTBLACK_EX + """Don't compare yourself with anyone in this world...""")
  print(Fore.RED + "if", Fore.WHITE + "you", Fore.RED + 'do so'+Fore.WHITE+",", Fore.RESET + 'you are insulting yourself.'+Fore.LIGHTBLACK_EX+'"')
  print(Fore.WHITE + "Bill Gates")

task1()

def task2(a,b):
  for i in range(a,b):
    if i%2 == 0:
      print(i)

task2(1,11)

def task3(len, symbol, choice):
  string = ""
  string_2 = ""
  if choice:
    for _ in range(len):
      string += symbol
    for _ in range(len):
      print(string)
  else:
    for _ in range(len):
      string += symbol
      string_2 += " "
    print(string)
    string_2 = list(string_2)
    string_2[0] = symbol
    string_2[-1] = symbol
    string_2 = "".join(string_2)
    for _ in range(len-2):
      print(string_2)
    else:
      print(string)

task3(10, "*", True)

def task4(*args):
  min = args[0]
  for i in args:
    if i < min:
      min = i
  return min

print(task4(1,2,3,4,5,6,7,8,9,10))

def task5(a,b):
  count = 1
  if a > b:
    for i in range(b,a):
      count *= i
  else:
    for i in range(a,b):
      count *= i
  return count

print(task5(10,5))

def task6(number):
  number = str(number)
  number = list(number)
  return len(number)

print(task6(3456))

def task7(number):
  number = str(number)
  number1 = number
  number = list(number)
  number1 = list(number1)
  number1.reverse()
  if number[0::2] == number1[0::2]:
    return True
  else:
    return False

print(task7(123321))
