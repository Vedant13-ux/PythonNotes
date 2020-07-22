import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank +' of '+self.suit   

class Deck:
    def __init__(self):
        self.all_cards=[]

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)     

    def display_cards(self):
        for card in self.all_cards:
            print(card)
    def deal_one(self):
        return self.all_cards.pop()    

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)    

#GAme SetUp
player1=Player('Vedant')
player2=Player('Ujjwal')

new_deck=Deck()
new_deck.shuffle()

for card in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())


#Game Start

round_num=0
game_on=True
while game_on:
    round_num+=1
    print(f"Round Number {round_num}")

    if len(player1.all_cards)==0:
        print(f'{player1.name} Out Of Cards,{player2.name} Wins')
        game_on=False
        break
    if len(player2.all_cards)==0:
        print(f'{player2.name} Out Of Cards,{player1.name} Wins')
        game_on=False
        break

    #Start OF Round
    
    
    player1_cards=[]
    player1_cards.append(player1.remove_one())

    player2_cards=[]
    player2_cards.append(player2.remove_one())

    at_war=True

    while at_war:

        if player1_cards[-1].value>player2_cards[-1].value:
           player1.add_cards(player2_cards);
           player1.add_cards(player1_cards);
           at_war=False

        elif player2_cards[-1].value>player1_cards[-1].value:
            player2.add_cards(player1_cards);
            player2.add_cards(player1_cards);
            at_war=False

        else:
            print('WAR!')

            if len(player1.all_cards)<5:
                print(f"{player1.name} cannot declare War")
                print(f"{player2.name} Wins the Round")
                game_on=False
                break

            elif len(player2.all_cards)<5:
                print(f"{player2.name} cannot declare War")
                print(f"{player1.name} Wins the Round")
                game_on=False
                break
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())









