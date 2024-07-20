#task 1
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

if lines1 != lines2:
    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
            break
    else:
        print("Files are identical")


#task 2
with open('file1.txt', 'r') as f, open('file1.txt', 'r') as fnew:
    lines = f.readlines()
    text = fnew.read()

countcharacters = len(text)
countlines = len(lines)
textlowered = text.lower()
VowellettersEnglish = "aeiouy"
VowellettersUkrainian = "аеєиіїоуюя"
countgolosni = 0
countnegolosni = 0
countnumber = 0
for i in textlowered:
    if i in VowellettersEnglish or i in VowellettersUkrainian:
        countgolosni += 1
    else:
        countnegolosni += 1
    if i.isdigit():
        countnumber += 1

print(f"К-сть символів = {countcharacters}")
print(f"К-сть рядків = {countlines}")
print(f"К-сть голосних = {countgolosni}")
print(f"К-сть неголосних = {countnegolosni}")
print(f"К-сть чисел = {countnumber}")



#task 3
with open('file1.txt', 'r') as origfile:
    lines = origfile.readlines()

file2 = open('fileedited.txt', 'w+')
fileedited = lines[:-1]
file2.writelines(fileedited)
file2.close()


#task 4
with open('file1.txt', 'r') as f:
    lines = f.readlines()
    max_len = 0
    max_line = ""
    for line in lines:
        line_len = len(line.strip())
        if line_len > max_len:
            max_len = line_len
            max_line = line.strip()
    print(f"Довжина найдовшого рядка: {max_len} символів.")
    print(f"Найдовший рядок: {max_line}")

#task 5
count = 0
word = input("Введіть слово для пошуку: ")
with open("file1.txt", 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if i.lower() == word.lower():
                count += 1

print(f"Слово {word} було знайдено {count} разів.")

#task 6
old_word = input("Введіть слово для пошуку: ")
new_word = input("Введіть слово для заміни: ")
with open("file1.txt", 'r') as f, open("filenew.txt", 'w+') as f2:
    file_content = f.read()
    new_content = file_content.replace(old_word, new_word)
    f2.write(new_content)

print(f"Слово '{old_word}' було замінено на '{new_word}' в файлі.")