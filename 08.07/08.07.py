import random
#task 1
def task1(a, b):
    if b == 0:
        return a
    else:
        return task1(b, a % b)

print(task1(12, 18))

#task 2
def count_bulls_and_cows(guess, number):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == number[i]:
            cows += 1
        elif guess[i] in number:
            bulls += 1
    return bulls, cows

def game(number, attempts=0):
    guess = input("Введіть 4-ьох значне число: ")
    if len(guess) != 4 or not guess.isdigit():
        print("Некоректний ввід. Будь ласка, введіть 4-значне число.")
        return game(number, attempts)
    attempts += 1
    bulls, cows = count_bulls_and_cows(guess, number)
    print(f"Бики: {bulls}, Корови: {cows}")
    if cows == 4:
        print(f"Вітаю! Ти виграв з {attempts} спробами.")
    else:
        return game(number, attempts)

print('Правила гри "Бики та Корови":\nВ чисельній версії програма задумує чотиризначне число (можливі варіанти з використанням числа будь-якої довжини). Всі цифри повинні бути різні. Тоді ж, в свою чергу, гравці намагаються вгадати число противника. Гравець пропонує свій варіант, а опонент дає кількість збігів. Якщо збігається цифра в її правильній позиції, то це є «корова», якщо не в своїй позиції — це «бик».') #маленький бонус(правила гри)
number = str(random.randint(1000, 9999))
game(number)


#task 3
def is_valid_move(board, x, y, moves):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return False
    if board[x][y] == 1:
        return False
    for move in moves:
        if (x, y) == move:
            return False
    return True

def get_possible_moves(board, x, y):
    moves = []
    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(board, new_x, new_y, moves):
            moves.append((new_x, new_y))
    return moves

def get_next_move(board, x, y, moves):
    possible_moves = get_possible_moves(board, x, y)
    if not possible_moves:
        return None
    next_move = min(possible_moves, key=lambda move: len(get_possible_moves(board, move[0], move[1])))
    return next_move

def solve_knight_tour(board, x, y, moves, move_num):
    if move_num == len(board) * len(board[0]):
        return True
    next_move = get_next_move(board, x, y, moves)
    if next_move is None:
        return False
    board[next_move[0]][next_move[1]] = 1
    moves.append(next_move)
    if solve_knight_tour(board, next_move[0], next_move[1], moves, move_num + 1):
        return True
    board[next_move[0]][next_move[1]] = 0
    moves.pop()
    return False

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

def main():
    board_size = int(input("Enter the size of the board: "))
    board = [[0] * board_size for _ in range(board_size)]
    x = int(input("Enter the x-coordinate of the starting position: "))
    y = int(input("Enter the y-coordinate of the starting position: "))
    board[x][y] = 1
    moves = [(x, y)]
    if solve_knight_tour(board, x, y, moves, 1):
        print("Solution found:")
        print_board(board)
        print("Path:", moves)
    else:
        print("No solution found.")

main()


#task 4

items = {}
position = None

def main_frame():
    d = items
    print(d[1], d[2], d[3], d[4])
    print(d[5], d[6], d[7], d[8])
    print(d[9], d[10], d[11], d[12])
    print(d[13], d[14], d[15], d[16])

def format(ch):
    ch = ch.strip()
    if len(ch) == 1:
        return '  ' + ch + '  '
    elif len(ch) == 2:
        return '  ' + ch + ' '
    elif len(ch) == 0:
        return '     '

def change(to):
    global position
    fro = position
    for a, b in items.items():
        if b == format(str(to)):
            to = a
            break
    items[fro], items[to] = items[to], items[fro]
    position = to

def build_board():
    global position
    for i in range(1, 17):
        items[i] = format(str(i))
    tmp = 0
    for a, b in items.items():
        if b == '  16 ':
            items[a] = '     '
            tmp = a
            break
    position = tmp
    diff = 10
    for _ in range(diff):
        lst = valid_moves()
        lst1 = []
        for j in lst:
            lst1.append(int(j.strip()))
        change(lst1[random.randint(0, len(lst1)-1)])

def valid_moves():
    pos = position
    if pos in [6, 7, 10, 11]:
        return items[pos - 4], items[pos - 1], items[pos + 1], items[pos + 4]
    elif pos in [5, 9]:
        return items[pos - 4], items[pos + 4], items[pos + 1]
    elif pos in [8, 12]:
        return items[pos - 4], items[pos + 4], items[pos - 1]
    elif pos in [2, 3]:
        return items[pos - 1], items[pos + 1], items[pos + 4]
    elif pos in [14, 15]:
        return items[pos - 1], items[pos + 1], items[pos - 4]
    elif pos == 1:
        return items[pos + 1], items[pos + 4]
    elif pos == 4:
        return items[pos - 1], items[pos + 4]
    elif pos == 13:
        return items[pos + 1], items[pos - 4]
    elif pos == 16:
        return items[pos - 1], items[pos - 4]

def game_over():
    flag = False
    for a, b in items.items():
        if b == '     ':
            pass
        else:
            if a == int(b.strip()):
                flag = True
            else:
                flag = False
    return flag

build_board()
main_frame()
print('Enter 0 to exit')
while True:
    print('Hello user:\nTo change the position just enter the no. near it')
    lst = valid_moves()
    lst1 = []
    for i in lst:
        lst1.append(int(i.strip()))
        print(i.strip(), '\t', end='')
    print()
    x = int(input())
    if x == 0:
        break
    elif x not in lst1:
        print('Wrong move')
    else:
        change(x)
    main_frame()
    if game_over():
        print('You WON')
        break