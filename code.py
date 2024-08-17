import random

while True:
    user = str(input("Rock, Paper, or Scissors: ")).lower()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"]).lower()
    
    if computer_choice == user:
        keep_playing = str(input("It's a draw. Let's keep playing, Yes/No: ")).lower()
        if keep_playing == "no":
            break
    elif (computer_choice == "rock" and user == "paper") or (computer_choice == "paper" and user == "scissors") or (computer_choice == "scissors" and user == "rock"):
        print(f"Congrats, you won! I chose {computer_choice}")
        break
    else:
        keep_playing = str(input("You lost, let's keep playing! Yes/No: ")).lower()
        if keep_playing == "no":
            break
