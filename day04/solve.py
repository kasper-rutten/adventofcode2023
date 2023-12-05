class Card:
    def __init__(self, line: str) -> None:
        # example line: '''Card  14: 64 44 89 88  1 38 20 99  9 81 | 71 68 91 21 92 75 49 22 27 12  9 26 57 13 66 45 40 37 16  4 44 90 98 85 61\n'''
        header, body = line.split(':')
        self.index = int(header.split(' ')[-1])
        self.winning_numbers_string, self.my_numbers_string= body.split('|')
        self.winning_numbers = self.convert_to_number_array(self.winning_numbers_string.strip())
        self.my_numbers = self.convert_to_number_array(self.my_numbers_string.strip())
        self.score = self.compute_score(self.my_numbers, self.winning_numbers)
    
    def convert_to_number_array(self, inputstr: str) -> [int]:
        output = inputstr.split(' ')
        output = [x for x in output if x != '']
        return output

    def compute_score(self, my_numbers: [int], winning_numbers: [int]):
        score = 0
        for n in my_numbers:
            if n in winning_numbers:
                score *= 2
                if score == 0:
                    score = 1
        return score

with open('input') as f:
    lines = f.readlines()
    cards = []
    for line in lines:
        cards.append(Card(line))
    total_score = 0
    for card in cards:
        total_score += card.score
    print(total_score)
