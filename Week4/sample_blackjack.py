import random

b = "\033[34m"
y = "\033[33m"
g = "\033[32m"
r = "\033[31m"
rst = "\033[0m"
bld = "\033[1m"

def draw():
   cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
   hand = random.choice(cards) 
   return hand

def calculate(hand, point):
    if type(hand) == int:
        return point + hand
    if hand == 'J' or hand == 'Q' or hand == 'K':
        return point + 10
    else:
        point += 11
        if point > 21:
            return point - 10
        else:
            return point

def turn(role):    
    # player's turn
    print(g, "=" * 14, sep='')
    print(f"{role}'s turn!")
    print("=" * 14,"\033[0m", sep='')
    hand1 = draw()
    hand2 = draw()
    
    point = 0
    point = calculate(hand1, point)
    point = calculate(hand2, point)
    
    print(f"{role}'s hand: {y}{hand1}{rst} and {y}{hand2}{rst}. Point: {y}{point}{rst}")
    
    while True:
        command = input("Do you want to [hit] or [stand]?(h/s): ").lower()
        if command == 'h':
            hand = draw()
            print(f"{role} draw a {y}{hand}{rst}.", end=' ')
            point = calculate(hand, point)
            if point > 21:
                print(f"{r}{role} busts!{rst}")
                return -1
            print(f"Point: {y}{point}{rst}")
        elif command == 's':
            return point
        else:
            print(f"Invalid command! Type either h or s.")
    
def game():
    print("Welcome to BlackJack! This game needs 1 player and 1 dealer!")
       
    # player's turn
    player_point = turn("Player")
    
    # dealer's turn
    dealer_point = turn("Dealer")
    
    # Result printing
    player_message = f"{bld}{r}[BUSTED]{rst}" if player_point == -1 else f"{bld}{g}{player_point}{rst}"
    dealer_message = f"{r}[BUSTED]{rst}" if dealer_point == -1 else f"{bld}{g}{dealer_point}{rst}"
    print("="*43)
    print(f"FINAL POINT: Player = {player_message}, Dealer = {dealer_message}")
    if player_point > dealer_point:
        print(f"{b}Player wins!{rst}")
    elif player_point < dealer_point:
        print(f"{b}Dealer wins!{rst}")
    else:
        print("Tie!")
    print("="*43)

game()
    
    
    
    


