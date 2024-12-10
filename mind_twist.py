import random
import tkinter as tk

colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White', 'Gray']
score = 0
timeleft = 30
mode = "words"
current_round_type = None

def set_mode(level):
    global timeleft, mode
    mode = level
    time_label.config(text=f"Time left: {timeleft}")
    instructions.config(
        text=f"Chosen mode: {mode.upper()}. Press 'Q' to start."
    )

def next_colour():
    global score, timeleft, current_round_type

    if timeleft > 0:
        user_input = e.get().strip().lower()  # Clean user input
        correct_word = colours[0].lower()
        correct_color = colours[1].lower()

        # Check correctness based on current round type
        print(f"Correct word: {correct_word}, Correct color: {correct_color}")
        print(f"User input: {user_input}, Round type: {current_round_type}")

        if current_round_type == "word" and user_input == correct_word:
            score += 1
        elif current_round_type == "color" and user_input == correct_color:
            score += 1

        # Update score display
        score_label.config(text=f"Score: {score}")

        # Clear entry box for next round and repare the next round
        e.delete(0, tk.END)
        random.shuffle(colours)
        
        # Set a new round type for "mix" mode
        if mode == "mix":
            current_round_type = random.choice(["word", "color"])
        else:
            current_round_type = "word" if mode == "words" else "color"

        # Display the new prompt
        if current_round_type == "word":
            label.config(fg='black', text=colours[0])
            instructions.config(text="Enter the WORD of the text!")
        elif current_round_type == "color":
            label.config(fg=colours[1], text=colours[0])
            instructions.config(text="Enter the COLOR of the text!")

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

    scores = load_highest_scores()

    tk.Label(window2, text=f"WORDS: {scores['words']}", font=(font, 12)).pack()
    tk.Label(window2, text=f"COLORS: {scores['colors']}", font=(font, 12)).pack()
    tk.Label(window2, text=f"MIX: {scores['mix']}", font=(font, 12)).pack()

    window2.mainloop()

def continue_game(event):
    next_colour()

def start_game(event):
    global timeleft
    if timeleft == 30:
        countdown()
    next_colour()

window = tk.Tk()
font = 'Helvetica'
window.title("Mind Twist: Words and Colors")
window.geometry("375x300")
window.resizable(False, False)

instructions = tk.Label(window, text='Welcome to the game! Choose your mode!', font=(font, 12))
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

mode_frame = tk.Frame(window)
mode_frame.pack(pady=10)

tk.Button(mode_frame, text="Words", command=lambda: set_mode("words")).grid(row=0, column=0, padx=5)
tk.Button(mode_frame, text="Colors", command=lambda: set_mode("colors")).grid(row=0, column=1, padx=5)
tk.Button(mode_frame, text="Mix", command=lambda: set_mode("mix")).grid(row=0, column=2, padx=5)

window.mainloop()
