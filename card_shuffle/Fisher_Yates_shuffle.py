import random;

RANKS = ['Dimond', 'Heart', 'Spade', 'Club']
SUITS = [str(x) for x in range(2,11)] + ['J', 'Q', 'k', 'A']

Deck = []

for r in RANKS:
    for s in SUITS:
        Deck.append(r + ' ' + s)

for i in range(len(Deck)):
    random_index = random.randint(0, i)
    Deck[i], Deck[random_index] = Deck[random_index], Deck[i]

print(Deck)
    