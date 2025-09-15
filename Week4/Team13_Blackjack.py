"""
Made by Team 13 Members:
    - Richie Cedrick Adrian 
    - Jasmine Regina
    - Ivan Pratama
"""

import random

# Defines card suit constants
SPADE = ["A\u2660", "2\u2660", "3\u2660", "4\u2660", "5\u2660", "6\u2660", "7\u2660", "8\u2660", "9\u2660", "10\u2660", "J\u2660", "K\u2660", "Q\u2660"]
HEARTS = ["A\u2665", "2\u2665", "3\u2665", "4\u2665", "5\u2665", "6\u2665", "7\u2665", "8\u2665", "9\u2665", "10\u2665", "J\u2665", "K\u2665", "Q\u2665"]
CLUBS = ["A\u2663", "2\u2663", "3\u2663", "4\u2663", "5\u2663", "6\u2663", "7\u2663", "8\u2663", "9\u2663", "10\u2663", "J\u2663", "K\u2663", "Q\u2663"]
DIAMONDS = ["A\u2666", "2\u2666", "3\u2666", "4\u2666", "5\u2666", "6\u2666", "7\u2666", "8\u2666", "9\u2666", "10\u2666", "J\u2666", "K\u2666", "Q\u2666"]

# Defines Color Constants for each ANSI Color code used in format string
RED = '\x1b[91m'
GREEN = '\x1b[92m'
YELLOW = '\x1b[93m'
BLACK = '\x1b[30m'
RESET = '\x1b[0m'

def deal_card(deck):
    """Randomly deals a card from existing deck then removes drawn card from deck

    Args:
        deck (list): list of cards inside the 52 card deck

    Returns:
        str: card that has been drawn randomly
    """
    
    card = random.choice(deck)
    deck.remove(card) # Removes drawn card from deck
    return card

def calculate_score(hand):
    """Takes in hand as parameter and calculates the total points of the hand

    Args:
        hand (list): list of current cards in hand

    Returns:
        str: In cases where first 2 drawn cards total to 21, returns string "Blackjack"
        else
        int: the total points of all cards in hand
    """
    total = int()
    
    for card in hand: # Calculates the total points by checking first character in card string
        if card[0] in ["J", "K", "Q"]:
            total += 10
        elif card[0] == "A":
            if total > 21:
                total+=1
            else:
                total+=11
        elif len(card) == 2: # Calculates total for Card 2-9
            total += int(card[0])
        else: # Calculates total for Card 10
            total += int(card[0:2])
            
    # Checks if first 2 drawn cards total to 21
    if total == 21 and len(hand) == 2:
        return "Blackjack"
    
    return total

def compare(player_score, dealer_score):
    """Compares the final score of the player and the dealer

    Args:
        player_score (int): the final score of the player
        dealer_score (int): the final score of the dealer

    Returns:
        string: The game result based of score comparrison (win or lose or draw)
    """
    # In cases where first two drawn cards total to 21, calculated score will be a string valued "Blackjack"
    if isinstance(player_score, str) or isinstance(dealer_score, str):
        # Determine results when either one of the Player and the Dealer has Blackjack
        if dealer_score == "Blackjack" and player_score == "Blackjack":
            return f"{YELLOW}Both dealer and player has Blackjack! Draw!{RESET}"
        elif dealer_score == "Blackjack":
            return f"{RED}Dealer has Blackjack. Player lose!{RESET}"
        elif player_score == "Blackjack":
            return f"{GREEN}Blackjack! Player win!{RESET}"
        else:
            raise ValueError("FOR DEVELOPERS: player_score or dealer_score string given was not 'Blackjack'")
    
    # When no Blackjack occurs, determine results by comparing points
    else:
        if player_score > 21:
            return f"{RED}Player went over. Player lose!{RESET}"
        elif dealer_score > 21:
            return f"{GREEN}Dealer went over. Player win!{RESET}"
        elif player_score == dealer_score:
            return f"{BLACK}It's a draw!{RESET}"
        elif player_score > dealer_score:
            return f"{GREEN}Player win!{RESET}"
        else:
            return f"{RED}Player lose!{RESET}"

def play_blackjack(deck, turn):
    """Runs main game of blackjack
    Game Summary:
        Simulates a two player blackjack game, where player must try to draw cards with total points closest to 21
        One player is playing as "The Player" and the other as "The Dealer"
        Game is played with a deck of 52 Cards, when cards drawn it is removed from deck
        Player can choose to hit to draw more cards or stand to stop drawing
        
    Args:
        deck (list): List of cards inside a 52 card deck
        turn (string): A string referring to the Player or Dealer
    
    Returns:
        list: a list where the first element is the player's score and the second element is the player's hand
    """
    player_score = int()
    turn_over = False
    player_hand = [deal_card(card_deck), deal_card(card_deck)]
    
    while not turn_over:
        # Loops over the game and determines player choice while game is not over
        player_score = calculate_score(player_hand)
        
        print(f"{turn}'s Turn\nYour cards: {YELLOW}{player_hand}{RESET} \nCurrent score: {GREEN}{player_score}{RESET}")

        # Ends game in cases of Blackjack or player busted
        if player_score == "Blackjack":
            turn_over = True
            print(f"{YELLOW}{turn.upper()} HAS A BLACKJACK{RESET}\n")
        elif player_score > 21:
            print(f"{RED}{turn.upper()} WENT OVER, BUSTED{RESET}\n")
            turn_over = True

        # Game runs until player chooses stand
        else:
            print(f"\n========== Your move? hit / stand: ==========")
            
            should_continue = input().lower()
            if should_continue == "hit":
                player_hand.append(deal_card(deck))
            elif should_continue == "stand":
                turn_over = True
            else:
                print("Please enter, hit or stand\n")
                continue
            print("="*45)

    return [player_score, player_hand]

if __name__ == "__main__":
    print(f"{('='*45)}\n\t    {RED}Welcome to Blackjack!{RESET}\n{('='*45)}")
    game_running = True
    while True:
        # Runs game
        if game_running:
            card_deck = SPADE + HEARTS + CLUBS + DIAMONDS # Assigns card suits into a deck of 52 card
            
            # Runs the turn for both Player and Dealer one at a time
            player_result = play_blackjack(card_deck, "Player")
            dealer_result = play_blackjack(card_deck, "Dealer")
            
            # Outputs final results
            print(f"Your final hand: {YELLOW}{player_result[1]}{RESET}, final score: {GREEN}{player_result[0]}{RESET}")
            print(f"Dealer's final hand: {YELLOW}{dealer_result[1]}{RESET}, final score: {RED}{dealer_result[0]}{RESET}")
            print("="*16, "Game Result", "="*16)
            print(compare(player_result[0], dealer_result[0]))
            print("="*45)
            
            game_running = False
        
        # After game finishes running, asks player for rematch
        user_rematch = input("Do you want to play again? (Y/N): ").strip().upper()
        if user_rematch in ["Y", "YES"]:
            print("Starting new game...")
            game_running = True
            continue
        elif user_rematch in ["N", "NO"]:
            print("Game ending...")
            break
        else:
            print("Enter either Y/N, try again")
            continue