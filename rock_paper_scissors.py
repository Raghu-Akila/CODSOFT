from random import choice

choices = ["rock", "paper", "scissors"]

def comTurn():
    return choice(choices)

def userTurn():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def detWin(user_choice, com_choice):
    if com_choice == user_choice:
        return "It's a tie!"
        
    elif (user_choice == 'rock' and com_choice == 'scissors') or \
         (user_choice == 'scissors' and com_choice == 'paper') or \
         (user_choice == 'paper' and com_choice == 'rock'):
        return "You win!"
    
    else:
        return "Computer wins!"

def result():
    user_choice = userTurn()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return
    
    com_choice = comTurn()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {com_choice}")
    
    result = detWin(user_choice, com_choice)
    print(f"\n{result}")
    
    return result


userScore = 0
comScore = 0
noOfTie = 0
playAgain = "yes"

while playAgain == "yes":
    Result = result()
    
    if Result == "Computer wins!":
        comScore += 1
    elif Result == "You win!":
        userScore += 1
    elif Result == "It's a tie!":
        noOfTie += 1
    print(f"\nCurrent Score: You: {userScore} | Computer: {comScore} | Tie: {noOfTie}")
    
    playAgain = input("\nDo you want to play another round? (yes/no): ").lower()
    
    while playAgain != "yes" and playAgain != "no":
        playAgain = input("Enter correct choice (yes/no): ")


