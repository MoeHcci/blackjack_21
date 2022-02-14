from random import shuffle

class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, dep_value):

        self.balance = self.balance + dep_value
        print(f" {self.name}'s current balance is ${self.balance} after adding ${dep_value}")

    def withdraw(self, withdraw_value):
        if withdraw_value > self.balance:
            self.balance = self.balance
            print(f" {self.name}'s does not have enought money in the balance to withdraw ${withdraw_value}")
            print(f" Therefore, {self.name}'s current balance is going to remain the same at ${self.balance} ")
        else:
            self.balance = self.balance - withdraw_value
            print(f" {self.name}'s current balance is ${self.balance} after withdrawing ${withdraw_value}")

    def __str__(self):
        return (f" {self.name}'s current balance is ${self.balance}")


class Cards():
    ranks_global = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                    'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    suits_global = {'Hearts': 'Hearts', 'Diamonds': 'Diamonds', 'Clubs': 'Clubs', 'Spades': 'Spades'}

    ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King')

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.int_rank = Cards.ranks_global[rank]
        self.forced_suit = Cards.suits_global[suit]

    def __str__(self):
        # return (f"The current suit and rank combination are {self.suit} & {self.rank}, which is equal to {self.int_rank}")
        return (f'{self.rank} of {self.suit}')

    def add(self):
        return sum(self.int_rank)


class Deck():
    ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King')

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    def __init__(self):
        self.deck_list = []
        # this is the actual list, so when we assign a varilable to the class we need to call on this list
        # 1. the reson why Deck class does not take any inputs in __init__(self)
        ##because you want the user to have no control of the output of this class
        ##The output of this class will always be a list of 52 cards controled by the code in this class

        for x in Deck.suits:
            for y in Deck.ranks:
                collecting_indv_items = Cards(x, y)

                self.deck_list.append(collecting_indv_items)

    def shuffle_deck(self):
        return shuffle(self.deck_list)

    def remove_card(self):
        return self.deck_list.pop()

    def __len__(self):
        return len(self.deck_list)


def blacjack():
    # creating two objects from the Account function
    player_1 = Account('player_1', 500)
    house = Account('house', 10000)

    # creating the deck and shuffling the deck
    black_jack_deck = Deck()
    black_jack_deck.shuffle_deck()

    # clearing the output eveytime the code is run
    from IPython.display import clear_output
    clear_output()

    print('\n')

    # Creating a varilable that control the logic by a while loop
    # could have written while True, but we would have issues exiting from the nested while loops
    game_start = True
    while game_start == True:

        # each game the objects from the Accont function place a specific value
        # the player account must maintain a specific value within their accounts to play

        # making sure we enter an integer
        # while the choice is not a digiti we will keep asking for an input
        # Once it is a digit we will exit the while loop of bet_value1.isdigit() == False
        bet_value1 = 'wrong'
        while bet_value1.isdigit() == False:
            bet_value1 = (input('How much would you like to bet with ? '))

            if bet_value1.isdigit() == False:
                print('You must enter an integer!')

        bet_value = int(bet_value1)

        print('\n')

        if player_1.balance < bet_value:
            print('The player does not have enought funds to play')
            break
        else:
            print("The player has funds to play to player BLACK JACK !!!")
            player_1.withdraw(bet_value)
            house.withdraw(bet_value)

        print('\n')

        # the players section
        player_cards = []  # -> a list to hold the string representation of each card
        player_cards_int_list = []  # -> a list to hold the integers of the player_cards list
        player_cards.append(black_jack_deck.deck_list.pop())
        # adding the first card to the player_cards list from the deck
        player_cards.append(black_jack_deck.deck_list.pop())
        # adding the second card to the player_cards list from the deck
        print("The player's cards are: ")
        for x in player_cards:
            print(x)
            player_cards_int_list.append(x.int_rank)  # -> adding the integer of the cards from to the integer list
        player_cards_sum = sum(player_cards_int_list)
        # -> making a value equal to the sum of all cards in the integer list
        print(f"The player's sum is {player_cards_sum}")

        print('\n')
        # the bank or house's section
        # the same exact apporach, except that, when running the function only the frist card is printed
        house_cards = []
        house_cards_int_list = []
        house_cards.append(black_jack_deck.deck_list.pop())
        house_cards.append(black_jack_deck.deck_list.pop())
        print("The house's first card is: ")
        print(house_cards[0])
        for y in house_cards:
            house_cards_int_list.append(y.int_rank)
        house_cards_sum = sum(house_cards_int_list)

        print('\n')

        # The first while loop, which is a nested while loop, because it is inside the game_start while loop
        while sum(player_cards_int_list) < 21:
            k = input('Player (bet) or (pass) ? ')
            if k == 'bet':

                player_cards_int_list.clear()  # -> the integer list must be clearned so the sum isn't added each time
                player_cards.append(black_jack_deck.deck_list.pop())  # adding a new card as long as we are below 21

                for x in player_cards:
                    print(x)
                    player_cards_int_list.append(x.int_rank)
                player_cards_sum = sum(player_cards_int_list)
                print(player_cards_sum)
                # if the sum is still below 21 it will go back to the if statment no need for continue or pass

                if sum(player_cards_int_list) == 21:
                    print('player won and house lost')
                    player_1.deposite(bet_value * 2)  # The account function will be updated
                    str(player_1)
                    game_start = False  # making the main while false
                    break  # exiting from the nested while loop
                elif sum(player_cards_int_list) > 21:
                    print('player lost and house won')
                    house.deposite(bet_value * 2)
                    game_start = False
                    break
            elif k == 'pass':
                break

        # An if statment forces the game to stop if the player wins
        if sum(player_cards_int_list) == 21 or sum(player_cards_int_list) > 21:
            house_condition = False
        else:
            house_condition = True

        while sum(house_cards_int_list) < 21:

            if house_condition == True:
                house_cards_int_list.clear()
                house_cards.append(black_jack_deck.deck_list.pop())

                for x in house_cards:
                    print(x)
                    house_cards_int_list.append(x.int_rank)
                house_cards_sum = sum(house_cards_int_list)
                print(house_cards_sum)

                if sum(house_cards_int_list) == 21:
                    print('house won and player lost')
                    house.deposite(bet_value * 2)
                    str(player_1)
                    game_start = False
                    house_condition = False
                    break
                elif sum(house_cards_int_list) > 21:
                    print('house lost and player won')
                    player_1.deposite(bet_value * 2)
                    game_start = False
                    house_condition = False
                    break
            else:
                break


if __name__ == '__main__':
    blacjack()
