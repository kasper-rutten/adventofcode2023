class Game:
    def __init__(self, line: str) -> None:
        # example line: '''Game 33: 3 green, 1 blue, 9 red; 2 blue, 12 red, 4 green; 1 blue, 5 red, 1 green; 4 green, 5 red, 2 blue; 1 red, 2 blue, 3 green; 3 green, 3 red, 1 blue\n'''
        header, body = line.split(':')
        self.index = int(header.split(' ')[1])
        self.draws_raw = body.split(';')
        self.draws_green = []
        self.draws_blue = []
        self.draws_red = []
        for draw in self.draws_raw:
            self.draws_green.append(self.draws_by_colour(draw, 'green'))
            self.draws_blue.append(self.draws_by_colour(draw, 'blue'))
            self.draws_red.append(self.draws_by_colour(draw, 'red'))
        print(f"for line {line[:-1]}, found index {self.index} and split draws {self.draws_raw}. Found green,blue,red draws {self.draws_green},{self.draws_blue},{self.draws_red}")
    
    def draws_by_colour(self, draw: str, colour: str) -> int:
        # returns the numeric value corresponding to the colour passed as argument
        if colour in draw:
            return int(draw.split(colour)[0].split(',')[-1])
        return 0

with open('input') as f:
    lines = f.readlines()
    games = []
    for line in lines:
        games.append(Game(line))
    answer = 0
    for game in games:
        if max(game.draws_red) <= 12 and max(game.draws_green) <= 13 and max(game.draws_blue) <= 14:
            answer += game.index
    print(f"The answer is {answer}")
