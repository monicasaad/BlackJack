# import required modules
from art import logo
import random


# function to deal a card
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# function to calculate score
def calculate(player_cards):
    """Take a list of cards and calculate player's score"""
    # start with score = 0 and loop through player's cards to add scores from each card
    total_score = 0
    for score in player_cards:
        total_score += score
    # if player gets a blackjack (scores 21 with first two cards) set to 0
    if player_cards[0] + player_cards[1] == 21:
        total_score = 0
    # if player gets an Ace, and their score is greater than 21, replace its value from 11 to 1
    if 11 in player_cards and total_score > 21:
        ace_index = player_cards.index(11)
        player_cards[ace_index] = 1
        total_score -= 10
    return total_score


# function to check for lose
def lose_check(player_score, u_cards, u_score, c_cards, c_score):
    """Take player's score which is being checked for lose, as well as all players' cards and scores and check
     if player's score has gone above 21 and output final hands and scores"""
    if player_score > 21:
        print(f"Your final hand: {u_cards}, final score: {u_score}")
        print(f"Computer's final hand: {c_cards}, final score: {c_score}")
        return True


# function to check for win
def win_check(player_score, u_cards, u_score, c_cards, c_score):
    """Take player's score which is being checked for a Blackjack, as well as all players' cards and scores and
    output final hands and scores"""
    if player_score == 0:
        print(f"Your final hand: {u_cards}, final score: {u_score}")
        print(f"Computer's final hand: {c_cards}, final score: {c_score}")
        return True


# variable to keep track if player wants to play game
play_game = True


# keep going until player does not want to play a new game
while play_game:
    print(logo)

    # lists to keep track of players' cards
    user_cards = []
    computer_cards = []

    # deal first card for user and first card for computer
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

    # set computer score to value of first card drawn
    computer_score = computer_cards[0]

    # variable to keep track if user wants to keep drawing a card
    continue_drawing = True

    # variable to keep track if game over (user has won or lost)
    game_over = False

    # continue until player does not want to draw another card
    while continue_drawing:
        # deal second (first iteration)/ additional card for user
        user_cards.append(deal_card())

        # calculate user's score and check if they won or lost
        user_score = calculate(user_cards)
        if win_check(player_score=user_score, u_cards=user_cards, u_score=user_score, c_cards=computer_cards,
                     c_score=computer_score):
            print("You win with a BlackJack!")
            # set game_over to true to skip dealing for computer then exit loop
            game_over = True
            break

        if lose_check(player_score=user_score, u_cards=user_cards, u_score=user_score, c_cards=computer_cards,
                      c_score=computer_score):
            print("You went over. You lose.")
            # set game_over to true to skip dealing for computer then exit loop
            game_over = True
            break

        # calculate user score and output current cards and score to user
        print(f"Your cards: {user_cards}, current score: {user_score}")

        # display computer's first card
        print(f"Computer's first card: {computer_score}")

        # see if user wants to draw another card
        draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_again == "n":
            # set continue_drawing to False to stop looping if user doesn't want another card
            continue_drawing = False

    # if user has not won (Blackjack) or lost (gone over)
    while not game_over:
        # deal another card for computer and recalculate score
        computer_cards.append(deal_card())
        computer_score = calculate(computer_cards)

        # check if computer got Blackjack
        if win_check(player_score=computer_score, u_cards=user_cards, u_score=user_score, c_cards=computer_cards,
                     c_score=computer_score):
            print("Opponent has a BlackJack. You lose.")
            # exit loop to end round
            break

        # continue adding cards for computer until computer_score is at least 17 and recalculate score after adding
        # each card
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate(computer_cards)

        # check if computer_score has gone over 21
        if lose_check(player_score=computer_score, u_cards=user_cards, u_score=user_score, c_cards=computer_cards,
                      c_score=computer_score):
            print("Opponent went over. You win.")
            # exit loop to end round
            break

        # if neither player gets a Blackjack or goes above 21, output final cards and scores to user
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        # compare scores to determine which player won
        if user_score > computer_score and computer_cards != 0:
            print("You win")
        elif computer_score > user_score and user_score != 0:
            print("You lose")
        else:
            print("Draw")
        break

    # check if user wants to play another round
    play_again = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again == "n":
        # switch play_game to False to stop looping
        play_game = False
