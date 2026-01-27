import random 

def rock_paper_scissors():
    chooses = ["rock", "paper", "scissors"] 
    computer = random.choice(chooses) 
    user = input("Choose: rock, paper or scissors? ").lower() 

    if user not in chooses: 
        print("Escolha inválida!") 
        return 

    print(f"The computer choose: {computer}") 

    if user == computer: 
        print("draws!") 
    elif ( 
        (user == "rock" and computer == "scissors") or 
        (user == "paper" and computer == "rock") or 
        (user == "scissors" and computer == "paper") 
    ): 
        print("You win!") 
    else: 
        print("You lose!") 
    
rock_paper_scissors()
