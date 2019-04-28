class Card(object):
    """standard playing card"""

    def __init__(self, rank=2, suit=0):
        self.rank=rank
        self.suit=suit

    suit_names=['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names=[None, 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self,other):
        if self.rank>other.rank:
            return 1
        if self.rank<other.rank:
            return -1
        if self.suit>other.suit:
            return 1
        if self.suit<other.suit:
            return -1
        return 0

class Deck(object):
    """It's a deck!"""
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(rank,suit)
                self.cards.append(card)

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self,card):
        return self.cards.append(card)

    def shuffle_cards(self):
        random.shuffle(self.cards)
        
class Hand(Deck):
    """it's the hand extracted from a deck"""
    def __init__(self, label=''):
        self.cards=[]
        self.label=label
        

card1=Card(int(raw_input('culoare=')),int(raw_input('numar=')))
card2=Card(int(raw_input('culoare=')),int(raw_input('numar=')))

print card1
print card2

if card1 > card2:
    print card1, '>', card2
elif card1 < card2:
    print card1, '<', card2
else:
    print card1, '=', card2

print card1 > card2


deck1=Deck()
print deck1

hand=Hand('new hand')
print hand.cards
print hand.label
deck=Deck()
card=deck.pop_card()
hand.add_card(card)
print hand
