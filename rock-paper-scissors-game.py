import random 

user_score = 0
computer_score = 0 
Draw = 0

options = [ 'rock', 'paper', 'scissors']

while True:
    user_input = input("Enter Rock, Paper, Scissors or Q to quit ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    #rock = 0, paper = 1, scissors = 2
    
    computer_selection = options[random_number]
    print('Computer picked', computer_selection + '.')
    
    if user_input == computer_selection:
        print('Draw')
        Draw +=1
        
    elif user_input == 'rock' and computer_selection == 'scissors':
        print("You Won!")
        user_score +=1
    elif user_input == 'paper' and computer_selection == 'rock':
        print("You Won!")
        user_score +=1
    elif user_input == 'scissors' and computer_selection == 'paper':
        print("You Won!")
        user_score +=1    
        
    else:
        print("You lost!")
        computer_score +=1   
        
print("You won", user_score, "times")
print("Computer Won", computer_score, "times")
print("Draw", Draw, "times")
print("GG")
        