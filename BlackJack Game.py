import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def adjust_ace(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        ace_index = hand.index(11)
        hand[ace_index] = 1
        total = sum(hand)
    return total


def stand(ptotal, ctotal):
    if ptotal > 21:
        print("Dealer wins")
    elif ctotal > 21:
        print("You win!")
    elif ptotal > ctotal:
        print("You win!")
    elif ptotal < ctotal:
        print("Dealer wins")
    else:
        print("Its a draw")


can_continue=True

while can_continue:

    # player
    player_cards = random.choices(cards, k=2)
    player_total = adjust_ace(player_cards)

    print(f"Your cards: {player_cards}")
    print(f"Your total: {player_total}")

    print("=====================================")

    # dealer
    computer_cards = random.choices(cards, k=2)
    computer_total = adjust_ace(computer_cards)

    print(f"Dealer's first card: {computer_cards[0]}")

    # blackjack check
    if player_total == 21:
        print("Blackjack! You win!")
        break

    # player turn
    while player_total < 21:
        pick_card = input("Draw another card? 'y' or 'n': ").lower()

        if pick_card == 'y':
            new_card = random.choice(cards)
            player_cards.append(new_card)

            player_total = adjust_ace(player_cards)

            print(f"Your cards: {player_cards}")
            print(f"Your total: {player_total}")

            if player_total > 21:
                print("You went over the limit and lost ")
                break

        else:
            break

    # dealer turn
    while computer_total < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_total = adjust_ace(computer_cards)

    print("=====================================")
    print(f"Dealer cards: {computer_cards}")
    print(f"Dealer total: {computer_total}")

    stand(player_total, computer_total)

    can_continue = False