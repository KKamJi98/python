import random
from modules.clear import clear
from modules.art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
# card limit -> infinity

# The dealer must hit until their hand totals 17 or higher.


def deal_card():
    return random.choice(cards)


def calculate_score(card_list) -> int:
    score = sum(card_list)
    # ACE가 여러 장 있을 때
    ace_count = card_list.count(11)
    while ace_count > 0 and score > 21:
        score -= 10
        ace_count -= 1
    return score


def print_status(player_card_list, dealer_card_list):
    player_score = calculate_score(player_card_list)
    print(f"Your cards: {player_card_list}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_card_list[0]}")


def get_winner(player_card_list, dealer_card_list):
    player_score, dealer_score = calculate_score(player_card_list), calculate_score(
        dealer_card_list
    )
    print(f"Your final hand: {player_card_list}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_card_list}, final score: {dealer_score}")

    if player_score > 21:
        print("You Burst! Dealer wins 😡")
    elif dealer_score > 21:
        print("Dealer Burst! You Win 😁")
    elif player_score == dealer_score:
        print("It's a Draw 😅")
    elif player_score > dealer_score:
        print("You Win 😁")
    else:
        print("You Lose 😟")


def blackjack():
    finished = False

    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    while not finished:
        print_status(player_cards, dealer_cards)
        while True:
            choice = input(
                "Do you want to Hit or Stand? Please type 'hit' or 'stand': "
            ).lower()
            if choice in ["hit", "stand"]:
                break
            else:
                print("Invalid input. Please type 'hit' or 'stand'.")
        if choice == "hit":
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            if player_score > 21:
                break
        elif choice == "stand":
            finished = True
            while calculate_score(dealer_cards) < 17:
                dealer_cards.append(deal_card())
    get_winner(player_cards, dealer_cards)


clear()
print(logo)
while True:
    start_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_choice == "y":
        clear()
        blackjack()
    elif start_choice == "n":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid input. Please type 'y' or 'n'.")
