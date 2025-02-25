from tkinter import *
import random as random_lib

def play_game():
    player_move = player_choice.get()
    computer_move = moves[random_lib.randint(0, 2)]
    player_score = int(player_score_label.cget("text"))
    computer_score = int(computer_score_label.cget("text"))

    if player_move == computer_move:
        result_label.config(text=f"Tie! You both chose {player_move}")
    elif (player_move == "rock" and computer_move == "scissor") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissor" and computer_move == "paper"):
        result_label.config(text=f"You win! {player_move} beats {computer_move}")
        player_score += 1
    else:
        result_label.config(text=f"You lose! {computer_move} beats {player_move}")
        computer_score += 1

    player_score_label.config(text=f"{player_score}")
    computer_score_label.config(text=f"{computer_score}")
    player_choice_label.config(text=f"Your Choice: {player_move}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_move}")

# Initialize main window
game_window = Tk()
game_window.title("Rock Paper Scissors")

# Available moves
moves = ["rock", "paper", "scissor"]

# Instruction label
instruction_label = Label(game_window, text="Choose Rock, Paper, or Scissors and see if you can beat the computer.\nThe game keeps track of both your score and the computer's score.", font=('Arial', 12), wraplength=400, justify="center")
instruction_label.pack(pady=10)

# Welcome label
welcome_label = Label(game_window, text="Welcome to Rock Paper Scissors Game", font=('Arial', 16))
welcome_label.pack(pady=10)

# Move selection label
move_prompt_label = Label(game_window, text="Choose your move:", font=('Arial', 14))
move_prompt_label.pack()

# Player choice variable
player_choice = StringVar()

# Radio buttons for player choices
button_frame = Frame(game_window)
button_frame.pack(pady=10)

rock_radiobutton = Radiobutton(button_frame, text="Rock", value="rock", variable=player_choice, command=play_game, font=('Arial', 12))
rock_radiobutton.grid(column=0, row=0, padx=10)

scissor_radiobutton = Radiobutton(button_frame, text="Scissor", value="scissor", variable=player_choice, command=play_game, font=('Arial', 12))
scissor_radiobutton.grid(column=1, row=0, padx=10)

paper_radiobutton = Radiobutton(button_frame, text="Paper", value="paper", variable=player_choice, command=play_game, font=('Arial', 12))
paper_radiobutton.grid(column=2, row=0, padx=10)

# Result display label
result_label = Label(game_window, text="", font=('Arial', 14))
result_label.pack(pady=10)

# Score display
score_frame = Frame(game_window)
score_frame.pack(pady=10)

player_score_text_label = Label(score_frame, text="Your Score: ", font=('Arial', 14))
player_score_text_label.grid(column=0, row=0)

player_score_label = Label(score_frame, text="0", font=('Arial', 14))
player_score_label.grid(column=1, row=0)

computer_score_text_label = Label(score_frame, text="Computer Score: ", font=('Arial', 14))
computer_score_text_label.grid(column=2, row=0, padx=(20, 0))

computer_score_label = Label(score_frame, text="0", font=('Arial', 14))
computer_score_label.grid(column=3, row=0)

# Display chosen moves
choice_display_frame = Frame(game_window)
choice_display_frame.pack(pady=10)

player_choice_label = Label(choice_display_frame, text="Your Choice: ", font=('Arial', 14))
player_choice_label.grid(column=0, row=0, padx=10)

computer_choice_label = Label(choice_display_frame, text="Computer's Choice: ", font=('Arial', 14))
computer_choice_label.grid(column=1, row=0, padx=10)

# Exit button
exit_button = Button(game_window, text="Exit", command=game_window.quit, font=('Arial', 12))
exit_button.pack(pady=20)

# Run the application
game_window.mainloop()
