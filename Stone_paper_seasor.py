import random
while True:
    user_action = input("Enter a choice (stone, paper, seasor) : ")
    possible_action = ["stone", "paper", "seasor"]
    computer_choice = random.choice(possible_action)
    print(f"You choose {user_action}, Computer choose {computer_choice}")
    if user_action==computer_choice:
        print(f"Both chossed {user_action} So, its Tie")
    elif user_action == "stone":
        if(computer_choice == "paper"):
            print("paper cover Stone! you Lose")
        else:
            print("Stone smashes seasor! you Win")
    elif user_action == "paper":
        if(computer_choice == "stone"):
            print("paper cover Stone! you Win")
        else:
            print("Seasor cut Paper! you Lose")
    elif user_action == "seasor":
        if computer_choice == "stone":
            print("Stone smashes seasor! you Lose")
        else:
            print("seasorn cut paper! you Win")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break