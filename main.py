import random
from ascii_art import rock, paper, scissors

# rock_paper_scissors list
game_images = [rock, paper, scissors]

# user choice
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:"))
if 0 <= user_choose <= 2:
    print("User Choose")
    print(game_images[user_choose])

print("computer choose")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

# check user choice b/z user can enter any value below 0 or above 2.
if user_choose < 0 or user_choose >= 3:
    print("invalid input. You lose!")
elif user_choose == 0 and computer_choice == 2:
    print("You Win")
elif computer_choice == 2 and user_choose == 0:
    print("You lose")
elif user_choose > computer_choice:
    print("You Win")
elif computer_choice > user_choose:
    print("You Lose")
elif user_choose == computer_choice:
    print("it's a Draw")
