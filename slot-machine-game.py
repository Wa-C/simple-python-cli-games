'''
Game description: 

user will deposit some money,
if they will then their money will be added to their balance

betting on lines and spins

generate items 

'''
import random


#Global constant 
MAX_LINES = 3
MAX_BET = 100  #100$
MIN_BET = 1    #1$

ROWS = 3
COLS = 3

# These are the symbol of the reel (each column). A is most costly so is low in value(2). D is Cheap so is most in value (8)
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {  # These are the value multiplyer
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # column index 0 but line value will go up to check the value in every line
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet  #this is bet for every line. one line can win other line can lose
            winning_lines.append(line + 1)
            
    return winnings, winning_lines       

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):   #Transposing the matrix to make the columns vertical. columns are in Horizontal now  
        for i,column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()        
                
#Taking deposit from the user
def deposit():
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
                
        else: 
            print("Enter a number")     
            
    return amount     

def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=MAX_LINES :
                break
            else:
                print('Enter a valid number of lines')
                
        else: 
            print("Enter a number")     
            
     return lines   

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - {MAX_BET}')
                
        else: 
            print("Enter a number")     
            
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, Balance is : ${balance}")
        else:
            break    
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')
    #print(balance, lines)    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)  #These slots are basically columns
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print (f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)   # "*" This is splat / unpack operator
    return winnings - total_bet


def main():
    balance = deposit()  
    while True:
        print(f"CUrrent Balance is:${balance}")
        answer = input("Press enter to spin ( q to quit)")
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")
    
main()    