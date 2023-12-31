import random


overs = 0.0
innings = 1
computer_score = 0
computer_wickets = 0
user_score = 0
user_wickets = 0
user_decision = ''
computer_decision = ''

def toss():
    global toss_result, toss, user_decision, computer_decision
    while True:
        user_input = input("Enter your choice (1 for Heads / 2 for Tails): ")
        if user_input == '1':
            user_choice = "heads"
            break
        elif user_input == '2':
            user_choice = "tails"
            break
        else:
            print("Invalid input! Please enter '1' for Heads or '2' for Tails.")

    toss_result = random.choice(['heads', 'tails'])
    
    toss = 'user' if toss_result == user_choice else 'computer'

    if toss == 'user':
        global user_decision, computer_decision
        print("You won the toss!")
        while True:
            user_decision = int(input("Choose to bat (1) or bowl (2): "))
            if user_decision == 1:
                user_decision = 'bat'
                print(f"You chosed to {user_decision} first")
                break
            elif user_decision == 2:
                user_decision = 'bowl'
                print(f"You chosed to {user_decision} first")
                break
            else:
                print("Invalid input! Please choose '1' to bat or '2' to bowl.")
    else:
        print("Computer won the toss!")
        computer_decision = random.choice(['1', '2'])
        computer_decision = 'bat' if computer_decision == '1' else 'bowl'
        print(f"Computer chose to {computer_decision} first.")

def display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings):
    print(f"\nScoreboard: (Inning: {innings})")
    print(f"Your score: {user_score}/{user_wickets}")
    print(f"Computer's score: {computer_score}/{computer_wickets}")
    print(f"Overs bowled: {round(overs, 1)}\n")

# Condition 1 - user won the toss and choose to bat first
def condition1():
    global overs, user_score, user_wickets, computer_score, computer_wickets, innings
    print("\nBatting time:")
    print("You get 2 overs (12 balls) to set a target for the computer.")
    print("If the computer chases the target, the computer wins. If not, you win.")
    print("If both your and computer's score is the same, it's a tie.\n")
    
    overs = 0.0  # Reset overs for batting

    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if user_wickets == 2:
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to score: "))
            comp_inp = random.randint(1, 6)
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if user_inp == comp_inp:
                print("You are out")
                user_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                user_score += user_inp  # Increment user's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    print(f"Your batting over is finished, your final score is\n{user_score}/{user_wickets}")
    print(f"Computer has a target of {user_score + 1} runs!")

    overs = 0.0  # Reset overs for bowling

    print("\nBowling time:")
    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if computer_score > user_score:
                print("Computer won the match!")
                break
            if computer_wickets == 2:
                print("Congrats, You won the match!")
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            comp_inp = random.randint(1, 6)
            user_inp = int(input("Enter a number between 1-6 to take wicket: "))
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if comp_inp == user_inp:
                print("Computer is out")
                computer_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                computer_score += comp_inp  # Increment computer's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    if user_score == computer_score:
        print("The match is a tie!")
    elif computer_score > user_score:
        print("Computer won the match!")
    else:
        print("Congrats, You won the match!!")

# Condition 2 - user won the toss and choose to bowl first
def condition2():
    global overs, user_score, user_wickets, computer_score, computer_wickets, innings
    print("\nBowling time:")
    print("You get 2 overs (12 balls) and computer will set a target for you")
    print("If tyou chase the target, you win. If not, then computer win.")
    print("If both your and computer's score is the same, it's a tie.\n")
    
    overs = 0.0  # Reset overs for bowling

    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if computer_wickets == 2:
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to take wicket: "))
            comp_inp = random.randint(1, 6)
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if user_inp == comp_inp:
                print("Computer are out")
                computer_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                computer_score += comp_inp  # Increment computer's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    print(f"Your bowling over is finished, computer's final score is\n{computer_score}/{computer_wickets}")
    print(f"You have a target of {user_score + 1} runs!")

    overs = 0.0  # Reset overs for batting

    print("\nBatting time:")
    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if user_score > computer_score:
                print("Congrats, You won the match!")
                break
            if user_wickets == 2:
                print("Computer won the match")
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to score: "))
            comp_inp = random.randint(1, 6)
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if comp_inp == user_inp:
                print("You are out")
                user_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                user_score += user_inp  # Increment computer's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    if user_score == computer_score:
        print("The match is a tie!")
    elif computer_score > user_score:
        print("Computer won the match!")
    else:
        print("Congrats, You won the match!!")

# Condition 3 - computer won the toss and choose to bat first
def condition3():
    global overs, user_score, user_wickets, computer_score, computer_wickets, innings
    print("\nBowling time:")
    print("You get 2 overs (12 balls) and computer will set a target for you")
    print("If tyou chase the target, you win. If not, then computer win.")
    print("If both your and computer's score is the same, it's a tie.\n")
    
    overs = 0.0  # Reset overs for bowling

    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if computer_wickets == 2:
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to take wicket: "))
            comp_inp = random.randint(1, 6)
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if user_inp == comp_inp:
                print("Computer are out")
                computer_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                computer_score += comp_inp  # Increment computer's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    print(f"Your bowling over is finished, computer's final score is\n{computer_score}/{computer_wickets}")
    print(f"You have a target of {user_score + 1} runs!")

    overs = 0.0  # Reset overs for batting

    print("\nBatting time:")
    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if user_score > computer_score:
                print("Congrats, You won the match!")
                break
            if user_wickets == 2:
                print("Computer won the match")
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to score: "))
            comp_inp = random.randint(1, 6)
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if comp_inp == user_inp:
                print("You are out")
                user_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                user_score += user_inp  # Increment computer's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    if user_score == computer_score:
        print("The match is a tie!")
    elif computer_score > user_score:
        print("Computer won the match!")
    else:
        print("Congrats, You won the match!!")

# Condition 4 - computer won the toss and choose to bowl first
def condition4():
    global overs, user_score, user_wickets, computer_score, computer_wickets, innings
    print("\nBatting time:")
    print("You get 2 overs (12 balls) to set a target for the computer.")
    print("If the computer chases the target, the computer wins. If not, you win.")
    print("If both your and computer's score is the same, it's a tie.\n")
    
    overs = 0.0  # Reset overs for batting

    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if user_wickets == 2:
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            user_inp = int(input("Enter a number between 1-6 to score: "))
            comp_inp = random.randint(1, 6)
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if user_inp == comp_inp:
                print("You are out")
                user_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                user_score += user_inp  # Increment user's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    print(f"Your batting over is finished, your final score is\n{user_score}/{user_wickets}")
    print(f"Computer has a target of {user_score + 1} runs!")

    overs = 0.0  # Reset overs for bowling

    print("\nBowling time:")
    for over in range(2):  # 2 overs
        for ball in range(6):  # 6 balls in an over
            if computer_score > user_score:
                print("Computer won the match!")
                break
            if computer_wickets == 2:
                print("Congrats, You won the match!")
                break

            if overs == 0.6:
                overs = 1.1
            else:
                overs += 0.1  # Increment the overs by 0.1 at the start of each ball
            print(f"Here comes {round(overs, 1)}")  # Display overs in the desired format
            comp_inp = random.randint(1, 6)
            user_inp = int(input("Enter a number between 1-6 to take wicket: "))
            
            if user_inp < 1 or user_inp > 6:
                print("Invalid Option selected")
                continue
            
            if comp_inp == user_inp:
                print("Computer is out")
                computer_wickets += 1
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)
            else:
                computer_score += comp_inp  # Increment computer's score
                display_scoreboard(user_score, user_wickets, overs, computer_score, computer_wickets, innings)

    if user_score == computer_score:
        print("The match is a tie!")
    elif computer_score > user_score:
        print("Computer won the match!")
    else:
        print("Congrats, You won the match!!")


def main():
    print("Welcome to CRICKET GAME!\n")
    print("Toss time!!\n")
    toss()

    # Condition 1 - user won the toss and choose to bat first
    if toss == 'user' and user_decision == 'bat':
        condition1()

    # Condition 2 - user won the toss and choose to bowl first
    elif toss == 'user' and user_decision == 'bowl':
        condition2()

    # Condition 3 - computer won the toss and choose to bat first
    elif toss == 'computer' and computer_decision == 'bat':
        condition3()

    # Condition 4 - computer won the toss and choose to bowl first
    elif toss == 'computer' and computer_decision == 'bowl':
        condition4()

if __name__ == '__main__':
    main()
