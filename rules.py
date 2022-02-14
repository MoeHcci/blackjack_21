#The game rules
#1. one human player and one computer dealer
#1. The human player starts with a bank account and places a specific value of
#their money to bet then starts the game
#2. start with a normal deck of card that is shuffeled
#Notes and put later into specific points
#3. computer starts with one card face up and one card face down
#4. player starts with two cards face up
#5. the human player goes first
#The player can either hit or stay and either action will end their turn

#Scenario0,
#during the first term the player can win if they continously hit
#and get to 21
#scenario1,
#during the first term the player can busts if they continously hit
#and go over 21
#2. the computer's turn begins, after the player completes their turn
#and have not won or lost yet.
#Scenario 2
#if the player is still under 21 and it is the computer's turn
##then, the computer will keep hitting until the dealer reaches 21 and wins
#Scenario 3
##if the player is still under 21 and it is the computer's turn
##then, the computer will keep hitting untill they exceed 21 and busts

#special rules
#1. all face cards are equal to 10. Face cards are jacks, queen, and king
#2. aces are either equal to 1

#the logic
#1. the bank account class will run with a specific player's name and amount.
#2. the deck will be shuffled
#3. two new lists will be made:
#a. a player list
#b. a computer list
#4. the player will take the first two cards and print them
#5. the computer will take two cards and print only one of them
#6. the player will go first
#7. then the computer then will go
#8. if the player skips a turn the computer would go and so on until busts happen
#9. if the player wins, he will double his money. If he loses he will lose that money to the house