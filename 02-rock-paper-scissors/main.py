ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

LOSES = 0
DRAWS = 3
WINS = 6


FIGURES = {
    'A': ROCK,
    'X': ROCK,
    'B': PAPER,
    'Y': PAPER,
    'C': SCISSORS,
    'Z': SCISSORS
}


POINT_MAP = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}


MATCH_MAP = {
    ROCK: {
        PAPER: LOSES,
        ROCK: DRAWS,
        SCISSORS: WINS
    },
    PAPER: {
        SCISSORS: LOSES,
        PAPER: DRAWS,
        ROCK: WINS
    },
    SCISSORS: {
        ROCK: LOSES,
        SCISSORS: DRAWS,
        PAPER: WINS
    }
}


def score(a: str, b: str) -> int:
    a_fig, b_fig = FIGURES[a], FIGURES[b]
    return POINT_MAP[b_fig] + MATCH_MAP[b_fig][a_fig]


def run():
    with open('./input', mode='r') as buffer:
        lines = buffer.read().splitlines()

    total = 0
    for line in lines:
        codes = line.split()
        total += score(codes[0], codes[1])
    print(total)


########## PART 2 #############
REQUIRED_OUTCOME = {
    'X': LOSES,
    'Y': DRAWS,
    'Z': WINS
}


OUTCOME_MAP = {
    ROCK: {
        LOSES: SCISSORS,
        DRAWS: ROCK,
        WINS: PAPER
    },
    PAPER: {
        LOSES: ROCK,
        DRAWS: PAPER,
        WINS: SCISSORS
    },
    SCISSORS: {
        LOSES: PAPER,
        DRAWS: SCISSORS,
        WINS: ROCK
    }
}


def part_two():
    with open('./input', mode='r') as buffer:
        data = buffer.read()

    total = 0
    lines = data.split('\n')
    for line in lines:
        codes = line.split()
        opp_code, required_outcome_code = codes[0], codes[1]

        required_outcome = REQUIRED_OUTCOME[required_outcome_code]
        opp_figure = FIGURES[opp_code]
        required_figure = OUTCOME_MAP[opp_figure][required_outcome]
        total += required_outcome + POINT_MAP[required_figure]
    print(total)

if __name__ == "__main__":
    # run()
    part_two()
