class CamelCardHand:
    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.card_occurrences = {}
        for card in set(self.cards):
            self.card_occurrences[card] = self.cards.count(card)
        self.type = self.check_type(cards)


    def check_type(self, card_occurrences: dict) -> int:
        # checks for four-of-a-kind, full-house etc.
        # High card = 0
        # One pair = 1
        # Two pair = 2
        # Three of a kind = 3
        # Full house = 4
        # Four of a kind = 5
        # Five of a kind = 6
        if self.is_five_of_a_kind(self.card_occurrences):
            return 6
        elif self.is_four_of_a_kind(self.card_occurrences):
            return 5
        elif self.is_full_house(self.card_occurrences):
            return 4
        elif self.is_three_of_a_kind(self.card_occurrences):
            return 3
        elif self.is_two_pair(self.card_occurrences):
            return 2
        elif self.is_one_pair(self.card_occurrences):
            return 1
        return 0
    
    def is_five_of_a_kind(self, card_occurrences: dict) -> bool:
        if max(card_occurrences.values()) == 5:
            #print(f"Found five of a kind in {cards}")
            return True
        return False
    
    def is_four_of_a_kind(self, card_occurrences: dict) -> bool:
        if max(card_occurrences.values()) == 4:
            #print(f"Found four of a kind in {cards}")
            return True
        return False
    
    def is_full_house(self, card_occurrences: dict) -> bool:
        if max(card_occurrences.values()) == 3:
            if min(card_occurrences.values()) == 2:
                return True
        return False
    
    def is_three_of_a_kind(self, card_occurrences: dict) -> bool:
        if max(card_occurrences.values()) == 3:
                return True
        return False
    
    def is_two_pair(self, card_occurrences: dict) -> bool:
        if list(card_occurrences.values()).count(2) == 2:
                return True
        return False
    
    def is_one_pair(self, card_occurrences: dict) -> bool:
        if list(card_occurrences.values()).count(2) == 1:
                return True
        return False

    def card1_is_smaller(self, card1: str, card2: str) -> bool:
        order = "AKQJT98765432"
        return(order.find(card1) > order.find(card2))


    def tie_breaker(self, other: 'CamelCardHand') -> bool:
        for index, card in enumerate(self.cards):
            if card == other.cards[index]:
                #print(f"at index {index}, card strings {self.cards} and {other.cards} are the same")
                continue
            if self.card1_is_smaller(card, other.cards[index]):
                #print(f"tie breaker says {card} is less than {other.cards[index]}")
                return True
            return False
        return False

    def __lt__(self, other: 'CamelCardHand') -> bool:
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        return self.tie_breaker(other)
        



with open('input') as f:
    lines = f.readlines()
hands = []
for line in lines:
    cards, bid = line.strip().split(' ')
    hands.append(CamelCardHand(cards, bid))

total_payout = 0
hands.sort()
for idx, hand in enumerate(hands):
    hand.payout = hand.bid * (idx + 1)
    total_payout += hand.payout
    #print(f"Hand {hand.cards} is type {hand.type}, bid {hand.bid}, payout = {hand.payout}, multiplier {idx + 1}")

print(total_payout)
