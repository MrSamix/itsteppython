#task 1
def task1(text):
  char_freq = {}
  for char in text:
      if char in char_freq:
          char_freq[char] += 1
      else:
          char_freq[char] = 1
  return char_freq


line = "Hello World, and HELLO World!"
print(task1(line))

#task 2
def task2(dict1, dict2):
  merged_dict = {}
  for key in set(dict1) and set(dict2):
      if key in dict1 and key in dict2:
          merged_dict[key] = [dict1[key], dict2[key]]
      elif key in dict1:
          merged_dict[key] = dict1[key]
      else:
          merged_dict[key] = dict2[key]
  return merged_dict

dict1 = {"1":"2", "3":"4", "5":"6", "7":"8", "9":"10"}
dict2 = {"1":"2", "3":"4", "5":"6", "7":"8", "9":"11"}

print(task2(dict1, dict2))

#task 3
def task3(dict):
  inverted_dict = {}
  for key, value in dict.items():
      inverted_dict[value] = key
  return inverted_dict

print(task3(dict1))

#task 4
def task4(dict, reverse=False): #False за зростанням, True за спаданням. За замовчуванням False
  sorted_dict = {}
  for key in sorted(dict.keys(), reverse=reverse):
      sorted_dict[key] = dict[key]
  return sorted_dict
dict3 = {"2":"4", "1":"3", "43":"23", "52":"bratyxa", "10":"11"}
print(task4(dict3))
print(task4(dict3, True))

#task 5
def task5(dict, value):
  result = []
  for key, val in dict.items():
      if value in str(val):
          result.append(key)
  return result

dict4 = {'a': 'hello', 'b': 'world', 'c': 'hello world'}
print(task5(dict4, "hello"))

#task 6
def task6(list_of_tuples):
  return dict(list_of_tuples)

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
print(task6(list_of_tuples))

#task 7
def task7(list_of_tuples):
  grouped_dict = {}
  for key, value in list_of_tuples:
      if key in grouped_dict:
          grouped_dict[key].append(value)
      else:
          grouped_dict[key] = [value]
  return grouped_dict

list_of_tuples = [(1, 'a'), (2, 'b'), (1, 'c')]
print(task7(list_of_tuples))

#task 8
def task8(dict1, dict2):
  merged_dict = {}
  for key in set(dict1) and set(dict2):
      if key in dict1 and key in dict2:
          merged_dict[key] = dict1[key] + dict2[key]
      elif key in dict1:
          merged_dict[key] = dict1[key]
      else:
          merged_dict[key] = dict2[key]
  return merged_dict

dict1 = {'a': [1, 2], 'b': [3, 4]}
dict2 = {'a': [5], 'b': [6, 7]}

print(task8(dict1, dict2))

#task 9
def task9(dict):
  max_key = max(dict, key=dict.get)
  min_key = min(dict, key=dict.get)
  return f"Максимальне - {max_key}. Мінімальне - {min_key}"

dict5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(task9(dict5))

#task 10
def task10(dict):
  total_sum = 0
  for value in dict.values():
      if isinstance(value, dict):
          total_sum += task10(value)
      else:
          total_sum += value
  return total_sum
dict6 = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
print(task10(dict6))