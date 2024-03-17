import art
import random

def deal_card():
    """Return a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculating_score(card):
    """Take a list of cards and return the score calculated fram cards """
    if sum(card) == 21 and len(card)==2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score >21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    

def play_game():
    print(art.logo)

    user_cards = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:

        user_score = calculating_score(user_cards)
        computer_score = calculating_score(computer_card)

        print(f"your card: {user_cards}, current_score: {user_score}" )
        print(f"computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'Y to get another card, type 'N'to pass: ")
            if user_should_deal == 'Y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score !=0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculating_score(computer_card)


    print(f" your final hand: {user_cards}, final score : {user_score}")
    print(f" computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))        
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()               

