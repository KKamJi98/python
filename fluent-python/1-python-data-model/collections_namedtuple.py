import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __iter__(self):
        return iter(self._cards)
    
beer_card = Card('7', 'diamonds')
# print(beer_card)
print(f"{'beer_card':<15}=> {beer_card}")
# Card(rank='7', suit='diamonds')

deck = FrenchDeck()
print(f"{'len(deck)':<15}=> {len(deck)}")
# len(deck) => deck.__len__()

print(f"{'deck[0]':<15}=> {deck[0]}")
# Card(rank='2', suit='spades') 위에서 __getitem__을 정의 해줬기 때문에 가능 deck.__getitem__(0)

from random import choice
print(f"{'random cards':<15}=> {choice(deck)}")
# random cards => __getitem__을 선언 해줬기 때문에 sequence에서 항목을 무작위로 골라내는 random.choice()함수 사용 가능

print(f"{'slicing':<15}=> {deck[:3]}")
# __getitem__을 지정해줘서 slicing 도 가능

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(f"{'card':<15}=> {card}")
    
