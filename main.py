import random
import tkinter as tk

colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White', 'Gray']
score = 0
timeleft = 30
round_number = 1
mode = "words"

# Function to change the mode
def set_mode(level):
    global timeleft, colours, round_number, mode
    if level == "words":
        mode = "words"
        round_number = 1
    elif level == "colors":
        mode = "colors"
        round_number = 2
    elif level == "mix":
        mode = "mix"

    time_label.config(text=f"Time left: {timeleft}")
    instructions.config(
    text=(
        "Choosen mode: MIX" if mode == "mix" else
        "Choosen mode: WORDS" if round_number == 1 else
        "Choosen mode: COLORS"
    )
)


def next_colour():
    global score, timeleft, round_number

    instructions.config(text="Enter the WORD of the text!" if round_number == 1 else "Enter the COLOR of the text!")

    if timeleft > 0:
        user_input = e.get().lower()

        if mode == "mix":
            round_number = random.randint(1, 2)
            instructions.config(text="Enter the WORD of the text!" if round_number == 1 else "Enter the COLOR of the text!")

        # Word Game
        if round_number == 1:
            correct_word = colours[0].lower()
            if user_input == correct_word:
                score += 1

        # Color Game
        if round_number == 2:
            correct_color = colours[1].lower()
            if user_input == correct_color:
                score += 1

        e.delete(0, tk.END)
        random.shuffle(colours)

        # Change the display based on the round
        if round_number == 1:
            label.config(fg='black', text=colours[0])  # Show the word in black color
        elif round_number == 2:
            label.config(fg=colours[1], text=colours[0])  # Show text in color
        
        score_label.config(text=f"Score: {score}")

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text=f"Time left: {timeleft}")
        time_label.after(1000, countdown)
    else:
        scoreshow()


def record_highest_score(category, score):
    scores = load_highest_scores()
    if score > scores.get(category, 0):  
        scores[category] = score
        with open("highest_scores.txt", "w") as file:
            for key, value in scores.items():
                file.write(f"{key}:{value}\n")

def load_highest_scores():
    try:
        scores = {}
        with open("highest_scores.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(":") 
                scores[key] = int(value)  
        return scores
    except (FileNotFoundError, ValueError):
        return {"colors": 0, "words": 0, "mix": 0}
    
def scoreshow():
    record_highest_score(mode, score)
    window2 = tk.Tk()
    window2.title("HIGH SCORE")
    window2.geometry("300x200")

    scores = load_highest_scores()  # Load all scores once

    labelWords = tk.Label(window2, text=f"WORDS: {scores['words']}", font=(font, 12))
    labelWords.pack()

    labelColors = tk.Label(window2, text=f"COLORS: {scores['colors']}", font=(font, 12))
    labelColors.pack()

    labelMix = tk.Label(window2, text=f"MIX: {scores['mix']}", font=(font, 12))
    labelMix.pack()

    window2.mainloop()

def continue_game(event):
    next_colour()

def start_game(event):
    global timeleft, round_number
    if timeleft == 30:
        countdown()
    next_colour()


window = tk.Tk()
font = 'Helvetica'
window.title("Mind Twist: Words and Colors")
window.iconbitmap("color_game_icon.ico")
window.geometry("375x300")
window.resizable(False, False)


instructions = tk.Label(window, text='Welcome to game! Choose your mode!', font=(font, 12))
instructions.pack(pady=10)

score_label = tk.Label(window, text="Press 'Q' to start", font=(font, 12))
score_label.pack()

time_label = tk.Label(window, text=f"Time left: {timeleft}", font=(font, 12))
time_label.pack()

label = tk.Label(window, font=(font, 60))
label.pack(pady=20)

e = tk.Entry(window)
window.bind('<q>', start_game)
window.bind('<Return>', continue_game)
e.pack()

e.focus_set()

# Mode buttons
mode_frame = tk.Frame(window)
mode_frame.pack(pady=10)

words_button = tk.Button(mode_frame, text="Words", command=lambda: set_mode("words"))
words_button.grid(row=0, column=0, padx=5)

colors_button = tk.Button(mode_frame, text="Colors", command=lambda: set_mode("colors"))
colors_button.grid(row=0, column=1, padx=5)

mix_button = tk.Button(mode_frame, text="Mix", command=lambda: set_mode("mix"))
mix_button.grid(row=0, column=2, padx=5)

window.mainloop()
