# This program will simulate a Blackjack game with a dealer and a player. The user will take the role of the player and will be able to bet money. The player will be able to hit or stand. It will follow standard Blackjack rules.

"""
Goal: Get a hand value as close to 21 as possible without going over (busting).

Card Values:
Number cards (2-10): Face value
Face cards (Jack, Queen, King): 10 points
Ace: 1 or 11 (you choose)
Gameplay:
Dealing: Each player receives two cards face-up.
Player's Turn:
Hit: Ask for another card.
Stand: Keep your current hand.
Dealer's Turn:
The dealer must hit until their hand value is 17 or higher.
Winning:
Blackjack: If you get 21 with your first two cards (Ace and a 10-value card), you usually win 3:2.
Higher Hand: If your hand value is closer to 21 than the dealer's without busting, you win.
Dealer Busts: If the dealer goes over 21, all remaining players win.
Push: If both you and the dealer have the same hand value, it's a tie (push).
""" 

import random

def drawCard(deck): # this will draw a random card from the deck which is passed to the function
  index = random.randint(0, len(deck)-1) # this chooses a random index from the deck
  card = deck.pop(index) # this removes the card from the deck and assigns it to the variable "card"
  return card # this returns the card to the function and ends it

def calculateScore(hand):
  score = 0
  for card in hand:
    if card > 10:
      score += 10
    elif card != 1:
      score += card
    else:
      if score + 11 > 21:
        score += 1
      else:
        score += 11
  return score

def playerDraws(playerHand):
  playerHand.append(drawCard(deck))
  playerScore = calculateScore(playerHand)
  print(f"Your hand: {playerHand}\nValue: {playerScore}")
  return playerHand, playerScore
  
def dealerDraws(dealerHand):
  dealerHand.append(drawCard(deck))  
  dealerScore = calculateScore(dealerHand)
  print(f"Dealer's hand: {dealerHand}\nValue: {dealerScore}")
  return dealerHand, dealerScore

def determineWinner(playerScore, dealerScore):
  if (playerScore > dealerScore) and (playerScore <= 21):
    print("You had a better hand. You win!")
  if (playerScore < dealerScore) and (dealerScore <= 21):
    print("The dealer had a better hand. You lose. Better luck next time!")
  if playerScore == dealerScore:
    print("It's a tie!")

def gamePlay(): 
  global deck
  playerHand = []
  dealerHand = []
  
  playerHand.append(drawCard(deck))
  playerHand.append(drawCard(deck))
  dealerHand.append(drawCard(deck))
  dealerHand.append(drawCard(deck))
  playerScore = calculateScore(playerHand)
  dealerScore = calculateScore(dealerHand)
  playerBusted = False
  dealerBusted = False
  
  print(f"Your hand: {playerHand}\nValue: {playerScore}")
  print(f"Dealer's hand: [{dealerHand[0]}, *]")
  
  while True:
    choice = input("Would you like to hit or stand?\n")
    print()
    if choice == "hit":
      playerHand, playerScore = playerDraws(playerHand)
      if playerScore > 21:
        print("You busted.")
        playerBusted = True
        break
      if (dealerScore < 17): # Dealer draws if score is below 17
        dealerHand, dealerScore = dealerDraws(dealerHand)
        if dealerScore > 21:
          print(f"Dealer busted!")
          dealerBusted = True
          break
      print(f"Dealer's hand: {dealerHand}\nValue: {dealerScore}")
    elif choice == "stand":
      print(f"Your hand: {playerHand}\nValue: {playerScore}")
      print(f"Dealer's hand: {dealerHand}\nValue: {dealerScore}")
      while dealerScore <= 16 or (dealerScore == 17 and playerScore >= 17): # Dealer draws if score is below 17 or if score is 17 and player's score is 17 or higher
        dealerHand, dealerScore = dealerDraws(dealerHand)
        if(dealerScore > 21):
          print(f"Dealer busted!")
          dealerBusted = True
      break
    else:
      print("Invalid input. Please try again.")

  if not playerBusted and not dealerBusted:
    determineWinner(playerScore, dealerScore)
  elif playerBusted and not dealerBusted:
    print(f"You lose!")
  elif not playerBusted and dealerBusted:
    print(f"You win!")
  else:
    print(f"You both busted. It's a tie!")
  if len(deck) == 0: # Handle empty deck
    print("The deck is empty. Shuffling the discard pile...")
    deck = dealerHand + playerHand
    random.shuffle(deck)

def playAgain(): 
  while True:
    playAgain = input("Would you like to play again? (yes/no)\n")
    print()
    if playAgain.lower() == "yes":
      return True
    elif playAgain.lower() == "no":
      return False
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")
      
# code starts here
print(f"Welcome to Blackjack!\nThe goal of the game is to get a hand value as close to 21 as possible without going over (bust)\nYou and the dealer will each be dealt two cards.\nThe dealer will only reveal one of your cards. You will be able to hit or stand.\nIf you hit, you will be dealt another card.\nIf you stand, your hand will stay the same.\nThe dealer will then hit until their hand value is 17 or higher.\nThe player with the highest hand value without busting wins.\n")
deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
# This is a list of each of the cards in the deck. Each number represents a card. Ace is 1, Jack is 11, Queen is 12, King is 13. In Blackjack, the suit of the card does not matter. It only depends on the number of the card.

while True:
  random.shuffle(deck)
  gamePlay()
  if not playAgain():
    break