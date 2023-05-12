player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

print(f"{player1} vs {player2}")

available_options = ["Rock", "Paper", "Scissors"]

user1_choice = ""
user2_choice = ""

def get_user1_choice():
    user1_choice = input(f"{player1} please select one of the following options:\nRock\nPaper\nScissors: ")
    while user1_choice not in available_options:
        user1_choice = input("Enter your choice: ")
    return user1_choice

def get_user2_choice():
    user2_choice =  input(f"{player2} please select one of the following options:\nRock\nPaper\nScissors: ")
    while user2_choice not in available_options:
        user2_choice = input("Enter your choice: ")
    return user2_choice

def play_game():
    user1_choice = get_user1_choice()
    user2_choice = get_user2_choice()
    print(f"{player1} chose {user1_choice}")
    print(f"{player2} chose {user2_choice}")
    get_winner(user1_choice, user2_choice)

def get_winner(user1_choice, user2_choice):
    if user1_choice == "Rock" and user2_choice == "Paper":
        print("Paper wins")
    elif user1_choice == "Rock" and user2_choice == "Scissors":
        print("Rock wins")
    elif  user1_choice == "Paper" and user2_choice == "Scissors":
        print("Scissors wins")
    elif user1_choice == user2_choice:
        print("It's a tie")

play_game()



