from tkinter import *

bomb = 100
score = 0

press_return = True

def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text="")
        update_display()
        update_bomb()
        update_score()
        press_return = False

def update_display():
    global bomb
    global score
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif bomb> 0 and bomb < 50 or bomb == 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse :" + str(bomb))
    score_label.config(text="Score :" + str(score))
    fuse_label.after(100, update_display)
                       

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)

def update_score():
    global score
    score += 1
    if is_alive():
        fuse_label.after(2000, update_score)
        update_best_score()

def update_best_score():
    global score
    try:
        with open("best_score.txt", "r") as f:
            best_score = int(f.read())
    except FileNotFoundError:
        best_score = 0
    if score > best_score:
        with open("best_score.txt", "w") as f:
            f.write(str(score))

def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text="")
        update_display()
        update_bomb()
        update_score()
        press_return = False
        best_score_label.config(text="Best Score: " + get_best_score())

def get_best_score():
    try:
        with open("best_score.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "0"

def click():
    global bomb
    if is_alive():
        bomb += 1

def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text="Bang! Bang! Bang!")
        press_return = True
        return False
    else:
        return True

root = Tk()
root.title("Band Bang")
root.geometry("500x600")

label = Label(root, text="Press [Enter] to start the game", font=("Comic Sans MS", 12))
label.pack()

fuse_label = Label(root, text="Fuse :" + str(bomb), font=("Comic Sans MS", 14))
fuse_label.pack()
score_label = Label(root, text="Score :" + str(score), font=("Comic Sans MS", 14))
score_label.pack()

no_photo = PhotoImage(file="img_for_clicker/bomb_no.gif")
normal_photo = PhotoImage(file="img_for_clicker/bomb_normal.gif")
bang_photo = PhotoImage(file="img_for_clicker/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()
best_score_label = Label(root, text="Best Score: " + get_best_score(), font=("Comic Sans MS", 14))
best_score_label.pack()

click_button = Button(root, text="Click me", bg="#000000", fg="#FFFFFF", width=15, font=("Comic Sans MS", 14), command=click)
click_button.pack()


root.bind("<Return>", start)

root.mainloop()