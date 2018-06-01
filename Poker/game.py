import os
import random

def print_hand(hand):
    out = ""
    for card in hand:
        out += str(card) + "  "
    return out

#N is the number of players
def Five_Card_Stud(N=2):
    #You really can't play with more ppl bc there aren't enough cards
    if N > 4:
        return False

    deck = [    'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC',
                'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH',
                'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS',
                'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD'
            ]
    shuffle = random.sample(range(0,52),52)
    
    #each players hand is given by an index
    player_hands = []
    for i in range(0,N):
        player_hands += [shuffle[0:5]]
        shuffle = shuffle[5:]
    
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,N):
        temp = raw_input("Press enter to see Player " + str(i+1) + " input.")
        #printing player hand
        print
        print print_hand(player_hands[i])    
        print
        #making sure input is valid
        while True:
            discard = raw_input("Which cards do you want to replace? (ex. 0, 2, 1)\n")
            discard = discard.split()
            
        print
        temp = raw_input("Press enter to clear the terminal.") 
        os.system('cls' if os.name == 'nt' else 'clear')

Five_Card_Stud(2)
