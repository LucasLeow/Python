import random
# 0 - rock
# 1 - paper
# 2 - scissors
user_choice = int(
    input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors: "))
computer_choice = random.randint(0, 2)

if (user_choice == 0):
    user_str = "Rock"
elif (user_choice == 1):
    user_str = "Paper"
else:
    user_str = "Scissors"

if (computer_choice == 0):
    computer_str = "Rock"
elif (computer_choice == 1):
    computer_str = "Paper"
else:
    computer_str = "Scissors"

if (user_choice == computer_choice):
    print("Draw")
    print(f"You chose {user_str}, Computer chose {computer_str}")
elif (
    (user_choice == 0 and computer_choice == 2) or
    (user_choice == 1 and computer_choice == 0) or
    (user_choice == 2 and computer_choice == 1)
):
    print("User win!")
    print(f"You chose {user_str}, Computer chose {computer_str}")
else:
    print("Computer win!")
    print(f"You chose {user_str}, Computer chose {computer_str}")
